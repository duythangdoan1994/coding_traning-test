import json
import httplib2 as http
import time
import logging
from datetime import datetime
from elasticsearch import Elasticsearch


BIND_PATH = ""
BIND_METHOD_POST = "POST"
BIND_METHOD_GET = "GET"
BIND_HEADER = {'Accept': 'application/json', 'Content-Type': 'application/json; charset=UTF-8'}
BIND_BODY = ""


class ESREQUEST(object):
    def __init__(self):
        url = ["128.199.214.107:9200"]
        self.index = "courses"
        self.doc_type = "course"
        self.es = Elasticsearch(hosts=url)

    def insert(self, _id, bodys, doc):
        if doc == None or doc == "":
            doc_type = "users"
        else:
            doc_type = self.doc_type
        self.es.index(index=self.index, doc_type=doc_type, id=_id, body=bodys)

    def insert_course(self, bodys):
        self.es.index(index=self.index, doc_type=self.doc_type, id=bodys["_id"], body=bodys["_source"])

    def get(self):
        query = {"query": {"match_all": {}}}
        response = self.es.search(index=self.index, size=1000, doc_type=self.doc_type, body=query)
        f = open("edumall_course.json", "w")
        for hit in response["hits"]["hits"]:
            f.write(json.dumps(hit) + "\n")
        f.close()


if __name__ == "__main__":
    esrq = ESREQUEST()
    f = open("file.json", "r")
    while 1:
        line = f.readline()
        if line == None or line == "":
            break
        line = line.split("\n")[0]
        esrq.insert_course(json.loads(line))