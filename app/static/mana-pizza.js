function $(id) {
    return document.getElementById(id);
}

$("calculateSimpleButton").disabled = true
$("calculateAdvancedButton").disabled = true

$("calculateSimpleButton").addEventListener("click", function() {
    $("outputAdvancedDiv").classList.add("hidden");
    $("outputSimpleDiv").classList.add("hidden");
    $("errorsDiv").classList.add("hidden");

    var csrfToken = document.querySelector("meta[name='csrf-token']").content

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/calculate/simple", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrfToken);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                response = JSON.parse(xhr.responseText)
                $("outputSimpleLands").textContent = response["selected_lands"].join("\n");
                $("statsSimpleLandCount").textContent = response["land_count"];
                $("statsSimpleTotalCMC").textContent = response["cmc_total"];
                $("statsSimpleAvgCMC").textContent = response["cmc_avg_all"];
                $("statsSimpleAvgCMCNoLands").textContent = response["cmc_avg_wo_lands"];
                Object.keys(response["color_proportions"]).forEach(function(k){
                    if (response["color_proportions"][k] > 0){
                        $("statsSimplePercent" + k).textContent = k + ": " + (response["color_proportions"][k] * 100) + "%" + "\n";
                    }
                    else {
                        $("statsSimplePercent" + k).textContent = ""
                    }
                });
                $("outputSimpleDiv").classList.remove("hidden");
            } else if (xhr.status === 422) {
                response = JSON.parse(xhr.responseText)
                console.log(response["errors"])
                $("spanErrors").textContent = response["errors"].join("\n");
                $("errorsDiv").classList.remove("hidden");
            }
        }
    };
    xhr.send(
        JSON.stringify({
            commander: $("inputCommander").value,
            cards: $("inputCards").value.split("\n")
        })
    );
});

$("calculateAdvancedButton").addEventListener("click", function() {
    $("outputAdvancedDiv").classList.add("hidden");
    $("outputSimpleDiv").classList.add("hidden");
    $("errorsDiv").classList.add("hidden");

    var csrfToken = document.querySelector("meta[name='csrf-token']").content

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/calculate/advanced", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrfToken);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                response = JSON.parse(xhr.responseText)
                $("outputAdvancedLands").value = response["selected_lands"].join("\n");
                $("statsAdvancedLandCount").textContent = response["land_count"];
                $("statsAdvancedTotalCMC").textContent = response["cmc_total"];
                $("statsAdvancedAvgCMC").textContent = response["cmc_avg_all"];
                $("statsAdvancedAvgCMCNoLands").textContent = response["cmc_avg_wo_lands"];
                $("statsAdvancedLandbasePrice").textContent = response["landbase_price"];
                $("statsAdvancedDeckPrice").textContent = response["deck_price"];
                Object.keys(response["color_proportions"]).forEach(function(k){
                    if (response["color_proportions"][k] > 0){
                        $("statsAdvancedPercent" + k).textContent = k + ": " + (response["color_proportions"][k] * 100) + "%" + "\n";
                    }
                    else {
                        $("statsAdvancedPercent" + k).textContent = ""
                    }
                });
                $("outputAdvancedDiv").classList.remove("hidden");
            } else if (xhr.status === 422) {
                response = JSON.parse(xhr.responseText)
                console.log(response["errors"])
                $("spanErrors").textContent = response["errors"].join("\n");
                $("errorsDiv").classList.remove("hidden");
            }
        }
    };
    xhr.send(
        JSON.stringify({
            commander: $("inputCommander").value,
            cards: $("inputCards").value.split("\n"),
            parameters: {
                "card_price_limit": parseFloat($("inputPriceLimit").value)
            }
        })
    );
});

$("closeErrorsDiv").addEventListener("click", function() {
    $("errorsDiv").classList.add("hidden");
});

$("closeSimpleOutputDiv").addEventListener("click", function() {
    $("outputSimpleDiv").classList.add("hidden");
});

$("closeAdvancedOutputDiv").addEventListener("click", function() {
    $("outputAdvancedDiv").classList.add("hidden");
});

$("clearSimpleInputsButton").addEventListener("click", function() {
    $("inputCards").value = "";
    $("inputCommander").value = "";
});

$("clearAdvancedInputsButton").addEventListener("click", function() {
    $("inputCards").value = "";
    $("inputCommander").value = "";
    $("inputPriceLimit").value = "10";
});

$("inputCards").addEventListener("input", function() {
    if ($("inputCards").value == "" || $("inputCommander").value == "") {
        $("calculateSimpleButton").disabled = true
        $("calculateAdvancedButton").disabled = true
    } else {
        $("calculateSimpleButton").disabled = false
        $("calculateAdvancedButton").disabled = false
    }
});

$("inputCommander").addEventListener("input", function() {
    if ($("inputCards").value == "" || $("inputCommander").value == "") {
        $("calculateSimpleButton").disabled = true
        $("calculateAdvancedButton").disabled = true
    } else {
        $("calculateSimpleButton").disabled = false
        $("calculateAdvancedButton").disabled = false
    }
});

$('copyResult').addEventListener('click', function() {
    var text = $('outputAdvancedLands');
    text.select();
    text.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(text.value);
})

