import glob

def getAllFile():
    return(glob.glob("./factbook/geos/*.html"))

def getAllJSON():
    return(glob.glob("./JSON/*.json"))