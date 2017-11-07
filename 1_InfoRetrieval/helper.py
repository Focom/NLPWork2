import glob
import json
import re

def getAllFile():
    return(glob.glob("./factbook/geos/*.html"))


def getAllJSON():
    return(glob.glob("./JSON/*.json"))


def correctJSON(data):
    return (json.dumps(data))
    # get string with all double quotes


def getAnswer():
    patternNumber = re.compile("Q(\d\d?)")
    patternCountry = re.compile(" ([\w]*)")
    with open("response.txt") as f:
        for line in f:
            number = patternNumber.search(line).group(1)
            answer = patternCountry.search(line).group(1)
            writeAnswerToFile(number, answer)


def writeAnswerToFile(number, answer):
    with open('responses.json', 'r') as f:
        doc = json.load(f)
    doc["responses"][str(number)].append(answer)
    with open('responses.json', 'w') as f:
        json.dump(doc, f)

