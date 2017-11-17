import json
import helper
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def insertAllDocuments():
    fileNames = helper.getAllJSON()
    max = len(fileNames)
    i = 1
    for file in fileNames:
        content = json.load(open(file))
        # print (file)
        es.index(index="factbook", doc_type="country", id=i, body=content)
        i += 1


def getNameFromQuery(query):
    data = es.search(index="factbook", doc_type="country", body=query)
    result = []
    for i in range(0, len(data["hits"]["hits"])):
        result.append(data["hits"]["hits"][i]["_source"]["Name"])
    return result


def askQuestion(number):
    words = helper.getWordFromQuestion(number)
    # print(words)
    question = {
        "query": {
            "match": {
                "_all": {
                    "query": words,
                    "operator": "or",
                    "minimum_should_match": "79%"
                }
            }
        }
    }
    return getNameFromQuery(question)


def isDocumentRelevent(doc, expected, number):
    for correct in expected:
        if(doc == correct):
            return True
    return False


def getPrecision(number):
    nbCorrect = 0
    nbPassed = 1
    precision = []
    result = askQuestion(number)
    expected = helper.getResponse(number)
    for doc in result:
        # print(doc)
        if(isDocumentRelevent(doc, expected, number)):
            nbCorrect += 1            
            precision.append(nbCorrect / nbPassed)
        nbPassed += 1
    return precision

def getLocalMEAN(number):
    precisions = getPrecision(number)
    sum = 0
    longueur = len(precisions)
    if(longueur == 0):
        return 0
    for prec in precisions:
        sum += prec
    result = sum/longueur
    return result

def getMEAN():
    precisions = []
    for i in range (0,20):
        precisions.append(getLocalMEAN(i))
        print(precisions)
    return helper.getAverageArray(precisions)



print(getMEAN())
