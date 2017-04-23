nicosearch
==========

# This repository is no longer maintained!
because of the end of "新検索β".

[![Build Status](https://travis-ci.org/ymizushi/nicosearch.png?branch=master)](https://travis-ci.org/ymizushi/nicosearch)

The wrapper library for niconico search API with python.

# Install
```sh
pip install nicosearch # Python 2.7.x or later
pip3 install nicosearch # Python 3.4.x or later
```

# Usage
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nicosearch import SearchRequest, SearchQueryBuilder
query = SearchQueryBuilder(u'MMD').build()
print(SearchRequest(query).fetch().contents)

# add search option
query = SearchQueryBuilder(u'閃乱カグラ', frm=0, size=10).build()
print(SearchRequest(query).fetch().contents)

# shortcut function
from nicosearch import search
print(search(u'閃乱カグラ'))
```

# Update PyPI command
```sh
python setup.py register sdist upload
```
