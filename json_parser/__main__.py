from . import json_parser as jp

json_parser = jp.JsonParser('test.json')

print(len(json_parser[0]))
print(json_parser[0].get('age', None))
print(len(json_parser[0]))
