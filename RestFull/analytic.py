from elasticsearch import Elasticsearch
from pprint import pprint
import json
from bson import json_util


def search():
    esclient = Elasticsearch(['localhost:9200'])
    response = esclient.search(
        index = 'courses',
        body = {
            "size": 600,
            "from":0,
            "query":{
                "bool": {
                    "should": [
                        {"match": {"version": "public"}},
                        {"match": {"enabled": True}}
                    ],
                    "minimum_should_match": 2
                }
            }
        }
    )
    return response


def parsing(response):
    data = response['hits']['hits']
    with open('file.json', 'w') as f:
        for doc in data:
            doc = json.dumps(doc, default=json_util.default)
            f.write(doc + '\n')
        f.close()


if __name__ == '__main__':
    response = search()
    parsing(response)