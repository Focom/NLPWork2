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
        i+=1

# json = json.load(open('./JSON/Algeria.json'))

# es.index(index='test-index', doc_type='test', id=1, body=json)
# es.delete(index='test-index', doc_type='test',id=1)
# insertAllDocuments()


question = {
 "query": {
        "query_string" : {
            "query" : "+European nations with +viking ancestors",
            "fields": ["Intro","Geography"]
        }
    }
}

print(es.search(index="factbook", doc_type="country", body=question))
