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
        index = str(i)
        result["answers"][index] = answer(data["tests"][index])
    logging.info("My result :{}".format(result))
    return jsonify(result)

def answer(case):
    seats = case["seats"]
    people = case["people"]
    spaces = case["spaces"]
    remaining = seats - people - spaces*(people-1)
    temp = people + 1
    sol = 1
    for i in range(remaining):
        sol = sol * temp
        temp = temp + 1
    for j in range(remaining,0,-1):
        sol = sol / j
    return sol
