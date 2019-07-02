from . import dom_parser as dp

def json_file(filename):
    root = dp.parse(filename)['root']
    if isinstance(root, list):
        base = list
    else: base = dict

    class JsonFile(base):
        def __init__(self, root):
            super().__init__(root)

        def __getitem__(self, root):
            if isinstance(self, dict):
                item = super()
                for path in root.split('.'):
                    item = item.__getitem__(path)
                return item
            
            else:
                return super().__getitem__(root)
        
    return JsonFile(root)
