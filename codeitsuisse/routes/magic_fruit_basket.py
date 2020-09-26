import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluateSecretMessage():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");
    result = 0
    result = result + data["maApple"]*data["maApple"]*10
    result = result + data["maWatermelon"]*data["maWatermelon"]*10
    result = result + data["maBanana"*data["maBanana"]*10
    logging.info("My result :{}".format(result))
    return jsonify(data);





