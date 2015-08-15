#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from nicosearch import SearchQueryBuilder, SearchRequest

query = SearchQueryBuilder(u'MMD').build()
print(SearchRequest(query).fetch().contents)

# add search option
query = SearchQueryBuilder(u'閃乱カグラ', frm=0, size=10).build()
print(SearchRequest(query).fetch().contents)

from nicosearch import ContentsBuilder

query = SearchQueryBuilder(u'閃乱カグラ', frm=0, size=10).build()
print(ContentsBuilder(SearchRequest(query).fetch().contents).build())

# shortcut function
from nicosearch import search

print(search(u'閃乱カグラ'))
