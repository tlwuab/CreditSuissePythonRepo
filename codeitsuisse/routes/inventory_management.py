import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/social_distancing', methods=['POST'])
def evaluateInventoryManagement():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    result = [{ "searchItemName" : data[0]["searchItemName"], "searchResult" : []}]
    for item in data[0]["items"]:
        result[0]["searchResult"].append(operate(result[0]["searchItemName"], item))

    logging.info("My result :{}".format(result))
    return jsonify(result)

def operate(ref,item):
    # Insertion: 1, Deletion: 2, Substitution: 3
    pref = 0
    pitem = 0
    ref_len = len(ref)
    status_list = []
    while(pref < ref_len):
        if(ref[pref] != item[pitem]):