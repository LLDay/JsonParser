from . import json_parser as jp

json_file = jp.json_file('test.json')

print(len(json_file[0]))
print(json_file[0].get('age', None))
print(len(json_file[0]))
