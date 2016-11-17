from elasticsearch import Elasticsearch
import json


def search(term ):
    """
    """
    esclient = Elasticsearch(['localhost:9200'])
    response = esclient.search(
        index = 'courses',
        body = {
            "query":{
                "multi_match": {
                    "fields": ["name", "user.name"],
                    "query": term,
                    "type": "phrase_prefix",
                }
            },
        }
    )
    return response


def parsing(results):
    data = result['hits']['hits']
    for doc in data:
        print("%s ---- %s ----%s" % (doc["_source"]["name"], doc["_source"]["user"]["name"], doc["_source"]["version"]))


if __name__ == '__main__':
    result = search("d")
    parsing(result)

