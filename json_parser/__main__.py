from . import dom_parser as dp

print([str(v) for v in dp.get_json_tree('test.json')])
