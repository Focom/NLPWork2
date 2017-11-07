import glob
import json

def getAllFile():
    return(glob.glob("./factbook/geos/*.html"))

def getAllJSON():
    return(glob.glob("./JSON/*.json"))

def correctJSON(data):
    return (json.dumps(data)) 
    #get string with all double quotes