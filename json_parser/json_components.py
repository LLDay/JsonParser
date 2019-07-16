import re


def _json_str_value(value):
    if value == None:
        return 'null'

    if isinstance(value, str):
        return '"{0}"'.format(value)

    elif isinstance(value, bool):
        return {True: 'true',
                False: 'false'}[value]
    else:
        return '{0}'.format(value)


class JsonObject(dict):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def __str__(self):
        if not len(self):
            return '{}'
         
        s = '{\n'
        s += ',\n'.join('"{0}": {1}'.format(k, _json_str_value(v))
                        for k, v in self.items())
        s += '\n}'
        return s


class JsonDotNotation():
    def __init__(self, root):
        self._root = root

    def __getitem__(self, path):
        if '.' in path:
            item = self._root
            for key in path.split('.'):
                if isinstance(item, list):
                    item = item.__getitem__(int(key))
                else:
                    item = item.__getitem__(key)
            return item
        return self._root.__getitem__(path)

    def __setitem__(self, path, value):
        if ' ' in path:
            raise RuntimeError(
                'This kind of objects contains only single words')
        if '.' in path:
            item = self._root
            path_list = path.split('.')
            for key in path_list[:-1]:
                if isinstance(item, list):
                    item = item.__getitem__(int(key))
                else:
                    item = item.__getitem__(key)
            item.__setitem__(path_list[-1], value)
        else:
            self._root.__setitem__(path, value)


class JsonList(list):
    def __init__(self, *args):
        return super().__init__(args)

    def __str__(self):
        if not len(self):
            return '[]'

        multiline = '[\n'
        multiline += ',\n'.join('{0}'.format(_json_str_value(item)) for item in self)
        multiline += '\n]'
        return multiline
