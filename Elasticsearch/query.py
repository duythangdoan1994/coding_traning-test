import requests
import json
from pprint import pprint


def search(uri, term):
    condition = {}
    condition["enabled"] = True
    condition["version"] = "public"
    must = json.dumps(
        { "term" : {
            "enabled": condition.get("enabled") }
        },
        { "term": {
            "version": condition.get("public") }
        }
    )        

    query = json.dumps({
        "query": {
            "multi_match": {
                "fields": ["name", "user.name"],
                "query": term,
                "filter" :{"and" : must },
                "type": "phrase_prefix"
            }
        }
    })
    
    # print(query)
    response = requests.get(uri, data=query)
    result = json.loads(response.text)
    pprint(result)
    # return result


def format_results(result):
    data = result['hits']['hits']
    for doc in data:
        if doc["_source"]["version"] == "public" and doc["_source"]["enabled"] == True:
            print("%s ---- %s ----%s" % (doc["_source"]["name"], doc["_source"]["user"]["name"], doc["_source"]["version"]))


if __name__ == '__main__':
    uri_search = 'http://localhost:9200/courses/_search'
    search(uri_search, "se")
    # result = search(uri_search, "se")
    # format_results(result)
