import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/intelligent-farming', methods=['POST'])
def evaluateSecretMessage():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");
    for sample in data["list"]:
        sample["geneSequence"] = alter(sample["geneSequence"])
    
    logging.info("My result :{}".format(result))
    return jsonify(data);

def alter(seq):
    # count the numbers of each base
    numA, numT, numC, numG = 0,0,0,0
    for i in seq:
        if(i=='A'):
            numA = numA + 1
        elif(i=='T'):
            numT = numT + 1
        elif(i=='C'):
            numC = numC + 1
        elif(i=='G'):
            numG = numG + 1
    



