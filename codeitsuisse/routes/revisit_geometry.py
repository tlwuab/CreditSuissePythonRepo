import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/revisitgeometry', methods=['POST'])
def evaluateRevisitGeometry():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");
    result = []
    result = evaluateIntersect(data["shapeCoordinates"], data["lineCoordinates"])
    
    logging.info("My result :{}".format(result))
    return jsonify(result);

INF = 100000
def constructLine(points):
    
    if(points[1]["x"] == points[0]["x"]):
        m = INF
        b = points[1]["x"]
    else:
        m = (points[1]["y"]-points[0]["y"])/(points[1]["x"]-points[0]["x"])
        b = points[0]["y"] - m * points[0]["x"]
    return { "m" : m, "b" : b}

def findIntersect(edgepoints, linepoints):
    edge = constructLine(edgepoints)
    line = constructLine(linepoints)
    if(edge["m"]==INF):
        intersectx = edge["b"]
        intersecty = line["m"]*edge["b"] + line["b"]
        if((intersecty-edgepoints[0]["y"])*(intersecty-edgepoints[1]["y"])<0):
            return { "x" : round(intersectx, 2), "y" : round(intersecty, 2) }
        else:
            return
    elif(line["m"]==INF):
        intersectx = line["b"]
        intersecty = edge["m"]*line["b"] + edge["b"]
        if((intersecty-edgepoints[0]["y"])*(intersecty-edgepoints[1]["y"])<0):
            return { "x" : round(intersectx, 2), "y" : round(intersecty, 2) }
        else:
            return
    elif(edge["m"]==0):
        intersecty = edge["b"]
        intersectx = (edge["b"] - line["b"])/line["m"]
        if((intersectx-edgepoints[0]["x"])*(intersectx-edgepoints[1]["x"])<0):
            return { "x" : round(intersectx, 2), "y" : round(intersecty, 2) }
        else:
            return   
    elif(line["m"]==0):
        intersecty = line["b"]
        intersectx = (line["b"] - edge["b"])/edge["m"]
        if((intersectx-edgepoints[0]["x"])*(intersectx-edgepoints[1]["x"])<0):
            return { "x" : round(intersectx, 2), "y" : round(intersecty, 2) }
        else:
            return               
    else:     
        delta = line["m"] - edge["m"]
        if(delta == 0):
            return
        deltax = edge["b"] - line["b"]
        deltay = line["m"] * edge["b"] - line["b"] * edge["m"]
        intersectx = deltax / delta
        intersecty = deltay / delta
        if((intersectx-edgepoints[0]["x"])*(intersectx-edgepoints[1]["x"]) < 0 and (intersecty-edgepoints[0]["y"])*(intersecty-edgepoints[1]["y"]) < 0):
            return { "x" : round(intersectx, 2), "y" : round(intersecty, 2) }
        else:
            return





def evaluateIntersect(shapepoints, linepoints):
    result = []
    for i in range(len(shapepoints)):
        if(i==len(shapepoints)-1):
            intersect = findIntersect([shapepoints[i],shapepoints[0]],linepoints)
        else:
            intersect = findIntersect([shapepoints[i],shapepoints[i+1]],linepoints)
        if(intersect!=None or intersect not in result):
            result.append(intersect)
    return result
            



