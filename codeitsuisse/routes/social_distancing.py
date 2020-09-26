import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/social_distancing', methods=['POST'])
def evaluateSocialDistancing():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");
    result = {"answers" : {}}
    for i in range(len(data["tests"])):
        result["answers"][str(i)] = answer(data["tests"][str(i)])
    logging.info("My result :{}".format(result))
    return jsonify(result);

def answer(case):
    seats = case["seats"]
    people = case["people"]
    spaces = case["spaces"]
    remaining = seats - people - spaces*(people-1)
    temp = people + 1
    result = 1
    for i in range(remaining):
        result = result * temp
        temp = temp + 1
    for j in range(remaining,0,-1):
        result = result / j
    return result
