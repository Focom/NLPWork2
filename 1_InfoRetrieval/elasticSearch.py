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
    for i in range(0,len(data["hits"]["hits"])):
        result.append(data["hits"]["hits"][i]["_source"]["Name"])
    return result

def askQuestion(number):
    words = helper.getWordFromQuestion(number)
    question = {
        "query": {
                    "query_string" : {
                        "query" : words
                    }
                }
    }
    return getNameFromQuery(question)

def getPrecision(number):
    result = askQuestion(number)
    expected = helper.getResponse(number)
    total_result = len(result)
    total_expected = len(expected)
    score = 0
    for test in result:
        for correct in expected:
            if(test == correct):
                score +=1
    precision = score / total_result
    return precision

def getMAP():
    scores = []
    for i in range(0,20):
        scores.append(getPrecision(i))
    mean = helper.getAverageArray(scores)
    return mean / 20

print(getMAP())
