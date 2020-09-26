import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluateFruitWeight():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");
    estimate = 0
    estimate = estimate + (data["maApple"]*data["maApple"]*10)
    estimate = estimate + (data["maWatermelon"]*data["maWatermelon"]*10)
    estimate = estimate + (data["maBanana"]*data["maBanana"]*10)
    return str(estimate);





