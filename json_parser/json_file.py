from . import dom_parser as dp

class JsonObject(dict):
    def __getitem__(self, root):
        item = super()
        for path in root.split('.'):
            item = item.__getitem__(path)
        return item
        
class JsonList(list):
    pass

def json_file(filename):
    root = dp.parse(filename)
    return root
