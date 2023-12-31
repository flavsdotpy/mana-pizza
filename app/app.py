import os
from http import HTTPStatus

from flask import Flask, jsonify, render_template, request
from flask_wtf.csrf import CSRFProtect

from mana_pizza.smoother import ManaPizzaLandSmoother, ManaSmootherHelper, local_db

app = Flask(__name__)
app.secret_key = os.getenv("CSRF_KEY").encode()
csrf = CSRFProtect(app)
ManaSmootherHelper.load()

# Route to serve the main HTML page
@app.route("/")
def index():
    return render_template("index.html", last_update=local_db.get_last_updated())


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    smoother = ManaPizzaLandSmoother(commander=data["commander"], parameters=data["parameters"])
    lands = smoother.smooth_mana(data["cards"])
    return jsonify(
        errors=smoother.errors,
        cmc_total=smoother.total_cmc,
        cmc_avg_all=round(smoother.total_cmc / 99, 2),
        cmc_avg_wo_lands=round(smoother.total_cmc / (99 - len(lands)), 2),
        pip_count=smoother.pip_count,
        color_proportions=smoother.color_proportions,
        total_price=round(sum([l.price for l in lands]), 2),
        lands=[l.name for l in lands]
    ), HTTPStatus.OK if not smoother.errors else HTTPStatus.UNPROCESSABLE_ENTITY
