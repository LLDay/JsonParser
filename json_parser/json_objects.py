import re

class JsonObject(dict):
    pass

class JsonObjectNotation(dict):
    def __getitem__(self, path):
        if '.' in path:
            item = super()
            for key in path.split('.'):
                item = item.__getitem__(key)
            return item
        return super().__getitem__(path)

    def __setitem__(self, path, value):
        if ' ' in path:
            raise RuntimeError('This kind of objects contains only single words')
        if '.' in path:
            item = super()
            path_list = path.split('.')
            for key in path_list[:-1]:
                if not item.__contains__(key):
                    item.__setitem__(key, JsonObjectNotation())
                item = item.__getitem__(key)
            item.__setitem__(path_list[-1], value)
        else:
            super().__setitem__(path, value)
        
class JsonList(list):
    def __getattribute__(self, attr):
        match = re.match(r'^_(\d+)$', attr)
        if match:
            return super().__getitem__(int(match.group(1)))

        return super().__getattribute__(attr)

