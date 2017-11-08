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

def getWordFromQuestion(number):
    with open('questions.json', 'r') as f:
        doc = json.load(f)
    return doc["questions"][number]

def getResponse(number):
    with open('responses.json', 'r') as f:
        doc = json.load(f)
    return doc["responses"][str(number+1)]

def getAverageArray(array):
    total = 0
    for i in range(0,len(array)):
        total += array[i]
    return total/len(array)
    