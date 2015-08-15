# -*- coding: utf-8 -*-

import requests
import json

from .config import API_ENTRY_POINT, API_END_POINT


class SearchQueryBuilder(object):
    def __init__(self, keyword, **option):
        self.__query = {
            'query': keyword,
            'service': ['video'],
            'search': ['title'],
            'join': ['cmsid', 'title', 'view_counter'],
            'from': 0,
            'size': 10,
            'sort_by': 'view_counter',
            'issuer': 'nicosearcy.py',
            'reason': 'searching niconico with python'
        }
        for k, v in option.items():
            if k is 'frm':
                k = 'from'
            self.__query[k] = v

    def build(self):
        return self.__query


class SearchRequest(object):
    __URL = API_ENTRY_POINT + API_END_POINT
    __HEADERS = {'content-type': 'application/json'}

    def __init__(self, data, url=__URL):
        self.__data = data
        self.__url = url

    def fetch(self):
        return SearchResponse(requests.post(self.__url, data=json.dumps(self.__data), headers=self.__HEADERS))


class SearchResponse(object):
    @classmethod
    def __filter_contents(cls, text):
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

    def __init__(self, response):
        self.__response = response
        self.__contents = self.__filter_contents(self.__response.text)

    @property
    def contents(self):
        return self.__contents


class Content:
    def __init__(self, rowid, cmsid, title, view_counter):
        self.__rowid = rowid
        self.__cmsid = cmsid
        self.__title = title
        self.__view_counter = view_counter

    @property
    def rowid(self):
        return self.__rowid

    @property
    def cmsid(self):
        return self.__cmsid

    @property
    def title(self):
        return self.__title

    @property
    def view_counter(self):
        return self.__view_counter


class ContentsBuilder:
    def __init__(self, contents):
        self._contents = contents

    def build(self):
        return map(
            lambda x: Content(x['_rowid'], x['cmsid'], x['title'], x['view_counter']),
            self._contents
        )


def search(keyword, **option):
    query = SearchQueryBuilder(keyword, **option).build()
    return SearchRequest(query).fetch().contents
