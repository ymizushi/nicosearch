nicosearch
==========

The wrapper library of niconico search API with python.


# Install
```sh
pip install nicosearch
```

# Usage
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin  = codecs.getreader('utf_8')(sys.stdin)

from nicosearch import SearchRequest, SearchQueryBuilder
query = SearchQueryBuilder(u'閃乱カグラ').build()
print SearchRequest(query).fetch().get_contents()

# add seach option
query = SearchQueryBuilder(u'閃乱カグラ', from=0, size=1).build()
print SearchRequest(query).fetch().get_contents()
```
