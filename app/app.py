import os
from http import HTTPStatus

from flask import Flask, jsonify, render_template, request
from flask_wtf.csrf import CSRFProtect

from mana_pizza.smoother import ManaPizzaLandSmoother, ManaSmootherResultType, ManaSmootherHelper, local_db

app = Flask(__name__)
app.secret_key = os.getenv("CSRF_KEY").encode()
csrf = CSRFProtect(app)
ManaSmootherHelper.load()

# Route to serve the main HTML page
@app.route("/")
def index():
    return render_template("index.html", last_update=local_db.get_last_updated())


@app.route("/calculate/<result_type>", methods=["POST"])
def calculate(result_type):
    data = request.get_json()
    try:
        result_type = ManaSmootherResultType(result_type)
    except:
        return jsonify(errors=[f"Result type {result_type} not accepted"])
    smoother = ManaPizzaLandSmoother(commander=data["commander"], parameters=data.get("parameters", dict()))
    smoother.smooth_mana(data["cards"], result_type)
    if result_type == ManaSmootherResultType.SIMPLE:
        return jsonify(
            errors=smoother.errors,
            land_count=smoother.land_count,
            cmc_total=smoother.total_cmc,
            cmc_avg_all=smoother.cmc_avg_with_lands,
            cmc_avg_wo_lands=smoother.cmc_avg_wo_lands,
            pip_count=smoother.pip_count,
            color_proportions=smoother.color_proportions,
            selected_lands=smoother.selected_lands_with_count
        ), HTTPStatus.OK if not smoother.errors else HTTPStatus.UNPROCESSABLE_ENTITY
    elif result_type == ManaSmootherResultType.ADVANCED:
        return jsonify(
            errors=smoother.errors,
            land_count=smoother.land_count,
            cmc_total=smoother.total_cmc,
            cmc_avg_all=smoother.cmc_avg_with_lands,
            cmc_avg_wo_lands=smoother.cmc_avg_wo_lands,
            pip_count=smoother.pip_count,
            color_proportions=smoother.color_proportions,
            landbase_price=smoother.landbase_price,
            deck_price=smoother.deck_price,
            selected_lands=smoother.selected_lands_with_count
        ), HTTPStatus.OK if not smoother.errors else HTTPStatus.UNPROCESSABLE_ENTITY
