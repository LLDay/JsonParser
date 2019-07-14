import unittest
from json_parser.json_file import JsonFile

class JsonTester(unittest.TestCase):
    
    def setUp(self):
        self.t1 = JsonFile('test/jsons/t1.json')
        self.t2 = JsonFile('test/jsons/t2.json')

    def tearDown(self):
        self.t1.close()
        self.t2.close()

    def test_reading(self):
        sr = str(self.t1['configurations'])
        self.assertEqual(self.t1.__len__(), 2)
        self.assertEqual(len(self.t1), 2)
        self.assertEqual(len(self.t2), 5)

        self.assertEqual(self.t1['version'], '0.2.0')
        self.assertEqual(self.t1['configurations']['name'], 'Json_Parser')
        self.assertEqual(self.t1.d['configurations.name'], 'Json_Parser')
        self.assertIsNone(self.t1.d['configurations.subauthors'])

        self.assertEqual(self.t2._0["index"], 0)
        self.assertEqual(self.t2._1["index"], 1)

        self.assertEqual(self.t2._0['friends']._1['name'], 'Burnett Salinas')
        self.assertTrue(self.t2._3['latitude'] < -40)
        self.assertTrue(self.t2[3]['isActive'])

        self.assertTrue(self.t2.d['3.isActive'])
        
if __name__ == '__main__':
    unittest.main()
