from . import dom_parser as dp

def json_file(filename):
    root = dp.parse(filename)['root']
    if isinstance(root, list):
        base = list
    else: base = dict

    class JsonFile(base):
        def __init__(self, root):
            super().__init__(root)
        
    return JsonFile(root)
