import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/olympiad-of-babylon', methods=['POST'])
def evaluateSecretMessage():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");
    result = optimal(data)
    logging.info("My result :{}".format(result))
    return jsonify(result);


def optimal(d):
    nBooks = d["numberOfBooks"]
    nDays = d["numberOfDays"]
    sortedBook = d["books"].sort()
    sortedDays = d["days"].sort()
    optimalBooks = 0
    j = nBooks-1
    for i in range(len(sortedDays)):
        if optimalBooks == nBooks:
            break
        if sortedBook[i] >= sortedBook[j]:
            sortedBook[i] = sortedBook[i] - sortedBook[j]
            i = i - 1
            j = j - 1
            optimalBooks = optimalBooks + 1
    return { "optimalNumberOfBooks" : optimalBooks }


