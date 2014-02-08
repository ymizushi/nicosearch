#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

class TestSearchQueryBuilder(unittest.TestCase):
    def test_build(self):
        from search import SearchQueryBuilder
        result = SearchQueryBuilder(u'閃乱カグラ').build()
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
        self.assertEqual(result, expected)

        expected = { 'query'   : u'閃乱カグラ', }
        self.assertNotEqual(result, expected)
        
        with self.assertRaises(TypeError):
            result = SearchQueryBuilder()

class TestSearchRequest(unittest.TestCase):
    def test_fetch(self):
        from search import SearchRequest, SearchResponse

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

class TestSearchRequest(unittest.TestCase):
    def test__filter_contents(self):
        pass

if __name__ == '__main__':
    unittest.main()
