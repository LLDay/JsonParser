import unittest
import json_parser as jp

class JsonTester(unittest.TestCase):
    
    def setUp(self):
        self.t1 = jp.json_file('test/jsons/t1.json')
        self.t2 = jp.json_file('test/jsons/t2.json')

    def tearDown(self):
        pass

    def test_reading(self):
        json = jp.json_file('jsons/t1.json')
