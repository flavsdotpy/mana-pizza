function $(id) {
    return document.getElementById(id);
}

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

$("calculateButton").disabled = true

$("calculateButton").addEventListener("click", function() {
    $("outputDiv").classList.add("hidden");
    $("errorsDiv").classList.add("hidden");

    var csrfToken = document.querySelector("meta[name='csrf-token']").content

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/calculate", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrfToken);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                response = JSON.parse(xhr.responseText)
                $("outputLands").value = response["lands"].join("\n");
                $("spanTotalCMC").textContent = response["cmc_total"];
                $("spanAvgCMC").textContent = response["cmc_avg_all"];
                $("spanAvgCMCNoLands").textContent = response["cmc_avg_wo_lands"];
                $("spanPrice").textContent = response["total_price"];
                Object.keys(response["color_proportions"]).forEach(function(k){
                    if (response["color_proportions"][k] > 0){
                        $("spanPercent" + k).textContent = k + ": " + (response["color_proportions"][k] * 100) + "%" + "\n";
                    }
                    else {
                        $("spanPercent" + k).textContent = ""
                    }
                });
                $("outputDiv").classList.remove("hidden");
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

$("clearButton").addEventListener("click", function() {
    $("outputDiv").classList.add("hidden");
    $("errorsDiv").classList.add("hidden");
});

$("inputCards").addEventListener("input", function() {
    if ($("inputCards").value == "" || $("inputCommander").value == "") {
        $("calculateButton").disabled = true
    } else {
        $("calculateButton").disabled = false
    }
});

$("inputCommander").addEventListener("input", function() {
    if ($("inputCards").value == "" || $("inputCommander").value == "") {
        $("calculateButton").disabled = true
    } else {
        $("calculateButton").disabled = false
    }
});

$('copyResult').addEventListener('click', function() {
    var text = $('outputLands');
    text.select();
    text.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(text.value);
})

