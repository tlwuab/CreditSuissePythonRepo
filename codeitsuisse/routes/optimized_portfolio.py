import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/optimizedportfolio', methods=['POST'])
def evaluateOptimizedPortfolio():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    
    result = { "outputs" : [] }
    for i in range(len(data["inputs"])):
        info = data["inputs"][i]
        result["outputs"].append(opti(info))

    logging.info("My result :{}".format(result))
    return jsonify(result)

def myround(num):
    if(round(num,2)-int(num)>=0.45):
        num = int(num) + 1
    return num

def opti(d):
    min_OHR = 1
    min_NFC = 100000
    best_option = 0
    result = []
    for i in range(len(d["IndexFutures"])):
        if round(d["IndexFutures"][i]["CoRelationCoefficient"]*d["Portfolio"]["SpotPrcVol"]/d["IndexFutures"][i]["FuturePrcVol"], 3) <= min_OHR:
            best_option = i
    min_OHR = round(d["IndexFutures"][best_option]["CoRelationCoefficient"]*d["Portfolio"]["SpotPrcVol"]/d["IndexFutures"][best_option]["FuturePrcVol"],3)
    min_NFC = myround((d["IndexFutures"][i]["CoRelationCoefficient"]*d["Portfolio"]["SpotPrcVol"]/d["IndexFutures"][best_option]["FuturePrcVol"])*d["Portfolio"]["Value"]/(d["IndexFutures"][best_option]["IndexFuturePrice"]*d["IndexFutures"][best_option]["Notional"]))
    for i in range(len(d["IndexFutures"])):
        if round(d["IndexFutures"][i]["CoRelationCoefficient"]*d["Portfolio"]["SpotPrcVol"]/d["IndexFutures"][i]["FuturePrcVol"], 3) == min_OHR:
            temp_NFC = myround((d["IndexFutures"][i]["CoRelationCoefficient"]*d["Portfolio"]["SpotPrcVol"]/d["IndexFutures"][i]["FuturePrcVol"])*d["Portfolio"]["Value"]/(d["IndexFutures"][i]["IndexFuturePrice"]*d["IndexFutures"][i]["Notional"]))
            if(temp_NFC == min_NFC):
                result.append({ "HedgePositionName" : d["IndexFutures"][i]["Name"],"OptimalHedgeRatio" : min_OHR,"NumFuturesContract" : min_NFC })
    
    return result



