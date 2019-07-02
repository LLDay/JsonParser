import unittest
import json_parser as jp

class JsonTester(unittest.TestCase):
    
    def setUp(self):
        self.t1 = jp.json_file('test/jsons/t1.json')
        self.t2 = jp.json_file('test/jsons/t2.json')

    def tearDown(self):
        pass

    def test_reading(self):
        self.assertEqual(len(self.t1), 2)
        self.assertEqual(len(self.t2), 5)

        self.assertEqual(self.t1['version'], '0.2.0')
        self.assertEqual(self.t1['configurations']['name'], 'Python: Module')
        self.assertEqual(self.t1['configurations.name'], 'Python: Module')
