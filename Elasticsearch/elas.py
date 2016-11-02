from elasticsearch import Elasticsearch
import json


def search(term ):
    esclient = Elasticsearch(['localhost:9200'])
    response = esclient.search(
        index = 'courses',
        body = {
            "query":{
                "multi_match": {
                    "fields": ["name", "user.name"],
                    "query": term,
                    "type": "phrase_prefix"
                }
            },
            "highlight" : {
                "fields" : {
                    "content" : {
                        "fragment_size" : 150,
                        "number_of_fragments" : 3,
                        "no_match_size": 150}
                    }
            }
        }
    )
    return response


def parsing(results):
    data = result['hits']['hits']
    for doc in data:
        if doc["_source"]["version"] == "public" and doc["_source"]["enabled"] == True:
            print("%s ---- %s ----%s" % (doc["_source"]["name"], doc["_source"]["user"]["name"], doc["_source"]["version"]))


if __name__ == '__main__':
    result = search("d")
    parsing(result)
                
