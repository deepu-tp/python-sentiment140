from nose.tools import *
import unittest
import os
from sentiment140.api import Sentiment140API

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.api = Sentiment140API('')

    def tearDown(self):
        pass

    def test_simple_classify(self):
        result = self.api.classify("Same Shit Different Day")
        print result
        assert_equal(result['polarity'], 2)


    def test_bulk_classify_json(self):
        result = self.api.bulk_classify_json([
            {
                'text' : "No bounce no play. :(",
                'id' : '123',
                'query' : "play"
            },

            {

                'text' : "What a wonderful world!",
                'id' : '124',
                'query' : 'world'

            }
        ])
        assert_equal(result[0]['polarity'], 0)
        assert_equal(result[1]['polarity'], 4)

