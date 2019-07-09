import re

class JsonObject(dict):
    def __getattribute__(self, name):
        if (name == 'd'):
            return JsonDotNotation(self)
        return super().__getattribute__(name)

class JsonDotNotation():
    def __init__(self, root):
        self.root = root

    def __getitem__(self, path):
        if '.' in path:
            item = self.root
            for key in path.split('.'):
                if isinstance(item, list):
                    item = item.__getitem__(int(key))
                else:
                    item = item.__getitem__(key)
            return item
        return self.root.__getitem__(path)

    def __setitem__(self, path, value):
        if ' ' in path:
            raise RuntimeError('This kind of objects contains only single words')
        if '.' in path:
            item = self.root
            path_list = path.split('.')
            for key in path_list[:-1]:
                if not item.__contains__(key):
                    item.__setitem__(key, JsonDotNotation())
                item = item.__getitem__(key)
            item.__setitem__(path_list[-1], value)
        else:
            self.root.__setitem__(path, value)
        
class JsonList(list):
    def __getattribute__(self, attr):
        match = re.match(r'^_(\d+)$', attr)
        if match:
            return super().__getitem__(int(match.group(1)))

        if (attr == 'd'):
            return JsonDotNotation(self)

        return super().__getattribute__(attr)


