#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

class TestSearchQueryBuilder(unittest.TestCase):
    def test_build(self):
        from nicosearch import SearchQueryBuilder
        actual = SearchQueryBuilder(u'閃乱カグラ').build()
        expected = {
            'query'   : u'閃乱カグラ',
            'service' : ['video'],
            'search'  : ['title'],
            'join'    : ['cmsid', 'title', 'view_counter'],
            'from'    : 0,
            'size'    : 10,
            'sort_by' : 'view_counter',
            'issuer'  : 'nicosearcy.py',
            'reason'  : 'searching niconico with python'
            }
        self.assertEqual(actual, expected)
        
        with self.assertRaises(TypeError):
            actual = SearchQueryBuilder()

class TestSearchRequest(unittest.TestCase):
    def test_fetch(self):
        from nicosearch import SearchRequest, SearchResponse

        query = {
            'query'   : u'閃乱カグラ',
            'service' : ['video'],
            'search'  : ['title'],
            'join'    : ['cmsid', 'title', 'view_counter'],
            'from'    : 0,
            'size'    : 10,
            'sort_by' : 'view_counter',
            'issuer'  : 'nicosearcy.py',
            'reason'  : 'searching niconico with python'
            }
        self.assertTrue(isinstance(SearchRequest(query).fetch(), SearchResponse))

if __name__ == '__main__':
    unittest.main()
