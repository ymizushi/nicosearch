#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin  = codecs.getreader('utf_8')(sys.stdin)

class SearchQueryBuilder(object):
    def __init__(self, query, **option):
        self.query = {
            'query'   :query,
            'service' : ['video'],
            'search'  : ['title'],
            'join'    : ['cmsid', 'title', 'view_counter'],
            'from'    : 0,
            'size'    : 10,
            'sort_by' : 'view_counter',
            'issuer'  : 'nicosearcy.py',
            'reason'  : 'searching niconico with python'
            }
        for k,v in option:
            self.query[k] = v

    def build(self):
        return self.query

class SearchRequest(object):
    URL = 'http://api.search.nicovideo.jp/api/'
    HEADERS = {'content-type': 'application/json'}

    def __init__(self, data, url=URL):
        self.data = data
        self.url = url

    def fetch(self):
        import requests, json
        return SearchResponse(requests.post(self.url, data=json.dumps(self.data), headers=self.HEADERS))

class SearchResponse(object):
    def __init__(self, response):
        self._response = response
        self._contents = self._filter_contents(self._response.text)

    def _filter_contents(self, text):
        import json
        json_list = text.splitlines()

        json_object_list = []
        for json_object in json_list:
            json_object_list += [json.loads(json_object, 'utf-8')]

        contents = []
        for json_object in json_object_list:
            if 'values' in json_object.keys():
                for value in json_object['values']:
                    if 'cmsid' in value.keys():
                        contents += [value]
        return contents

    def get_contents(self):
        return self._contents

