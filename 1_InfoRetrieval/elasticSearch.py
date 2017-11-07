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

question = {
    "query": {
        "bool" : {
            "must" : {
                "query_string" : {
                    "query" : "island"
                }
            }
    }
}}




# print(es.search(index="factbook", doc_type="country", body=question))
