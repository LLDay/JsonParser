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

    def _reach_parent_node(self, path):
        if ' ' in path:
            raise RuntimeError(
                "Path shuldn't contain spaces")

        parent = self._root
        if '.' in path:
            path_list = path.split('.')
            for key in path_list[:-1]:
                if isinstance(parent, list):
                    parent = parent.__getitem__(int(key))
                else:
                    parent = parent.__getitem__(key)

        if isinstance(parent, list):
            return parent, int(path_list[-1])
        return parent, path_list[-1]

    def __getitem__(self, path):
        parent, path = self._reach_parent_node(path) 
        return parent[path]

    def __setitem__(self, path, value):
        parent, path = self._reach_parent_node(path)
        parent[path] = value
        

class JsonList(list):
    def __init__(self, *args):
        return super().__init__(args)

    def __str__(self):
        if not len(self):
            return '[]'

        multiline = '[\n'
        multiline += ',\n'.join('{0}'.format(_json_str_value(item))
                                for item in self)
        multiline += '\n]'
        return multiline
