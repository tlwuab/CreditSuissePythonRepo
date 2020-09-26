import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/olympiad-of-babylon', methods=['POST'])
def evaluateOptimal():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");
    result = optimal(data)
    logging.info("My result :{}".format(result))
    return jsonify(result);


def optimal(d):
    nBooks = d["numberOfBooks"]
    nDays = d["numberOfDays"]

    sortedBook = d["books"]
    sortedBook.sort(reverse=True)
    sortedDays = d["days"]
    sortedDays.sort(reverse=True)

    # current minimum book without being taken
    minIndex = nBooks-1
    optimalBooks = 0

    optimallist = []
    for i in range(nDays): 
        sortedDays[i] = sortedDays[i] - sortedBook[start]
        optimalBooks = optimalBooks + 1
        start = start + 1
        while(sortedDays[i]>=sortedBook[end]):
            sortedDays[i] = sortedDays[i] - sortedBook[end]
            optimalBooks = optimalBooks + 1
            end = end - 1
    return { "optimalNumberOfBooks" : optimalBooks }


