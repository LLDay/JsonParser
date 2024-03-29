import unittest
from json_parser import *

class JsonTester(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_reading(self):
        t1 = JsonFile('resources/t1.json')
        t2 = JsonFile('resources/t2.json')
        self.assertEqual(len(t1), 2)
        self.assertEqual(len(t2), 5)

        self.assertEqual(t1['version'], '0.2.0')
        self.assertEqual(t1['configurations']['name'], 'Json_Parser')
        self.assertEqual(t1.d['configurations.name'], 'Json_Parser')
        self.assertIsNone(t1.d['configurations.subauthors'])

        self.assertEqual(t2[0]["index"], 0)
        self.assertEqual(t2[1]["index"], 1)

        self.assertEqual(t2[0]['friends'][1]['name'], 'Burnett Salinas')
        self.assertTrue(t2[3]['latitude'] < -40)
        self.assertTrue(t2[3]['isActive'])

        self.assertTrue(t2.d['3.isActive'])
        
        t1.close()
        t2.close()

    def test_example(self):
        t1 = JsonFile('resources/t1.json')
        t3 = JsonFile('resources/t3.json', root=t1.tree_copy())
        t1.close()

        del t3['configurations']['subauthors']
        del t3['version']

        t3['configurations']['type'] = 'Test'
        t3['new line'] = "I'm new line"
        t3['new object'] = JsonObject({'Hello': 'world'}, length=12.5)
        t3['new object']['temperature'] = 120.8
        t3['new list'] = JsonList(True, False, None)
        t3['new list'].extend([True, "Hello", 12, 0.3])
        t3['empty object'] = JsonObject()
        t3['empty list'] = JsonList() 
        t3.save().close()

        t3 = JsonFile('resources/t3.json')
        self.assertEqual(t3.d['configurations.type'], 'Test')
        self.assertTrue(t3['new list'][4])
        self.assertTrue('empty list' in t3)
        t3.close()

    def test_clear(self):
        t1 = JsonFile('resources/t1.json')
        root = t1.tree_copy()
        self.assertTrue(t1)

        t1.clear()
        self.assertFalse(t1)
        
        t1.clear(root)
        self.assertDictEqual(root, t1.tree_copy())
        
        t1.close()

    def test_dot_notation(self):
        t2 = JsonFile('resources/t2.json')
        self.assertEqual(t2.d['0.friends.0.name'], 'Stewart Vaughan')
        self.assertEqual(t2.d['3.tags.-1'], 'eiusmod')
        t2.close()

        t4 = JsonFile('resources/t4.json', JsonList())
        t4.append(JsonObject(key="value", list=JsonList(True, 8, None)))
        t4.d['0.new_key'] = 'new value'
        t4.d['0.list'].append(False)

        self.assertEqual(t4.d['0.list.1'], 8)
        self.assertEqual(len(t4.d['0.list']), 4)

        def assign():
            t4.d['0.undefined.path'] = 'value'

        self.assertRaises(KeyError, assign)
        t4.d['0.undefined'] = JsonObject()
        assign()
        self.assertEqual(t4.d['0.undefined.path'], 'value')
        t4.close()
        