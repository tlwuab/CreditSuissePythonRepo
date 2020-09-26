import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/optimizedportfolio', methods=['POST'])
def evaluateOptimizedPortfolio():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    
    info = data["inputs"][0]
    result = { "outputs" : [] }
    result["outputs"].append(opti(info))
    logging.info("My result :{}".format(result))
    return jsonify(result)

def opti(d):
    min_OHR = 1
    min_NFC = 0
    best_option = 0
    for i in range(len(d["IndexFutures"])):
        if d["IndexFutures"][i]["CoRelationCoefficient"]*d["Portfolio"]["SpotPrcVol"]/d["IndexFutures"][i]["FuturePrcVol"] < min_OHR:
            best_option = i
    min_OHR = round(d["IndexFutures"][best_option]["CoRelationCoefficient"]*d["Portfolio"]["SpotPrcVol"]/d["IndexFutures"][best_option]["FuturePrcVol"],3)
    min_NFC = int(round(min_OHR*d["Portfolio"]["Value"]/(d["IndexFutures"][best_option]["IndexFuturePrice"]*d["IndexFutures"][best_option]["Notional"]),0))
    return { "HedgePositionName" : d["IndexFutures"][best_option]["Name"], "OptimalHedgeRatio" : min_OHR, "NumFuturesContract" : min_NFC }
    



