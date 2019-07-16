import re
import os.path
import copy

from .dom_parser import parse
from .json_objects import *


class JsonFile:
    def __init__(self, filename, root=None):
        mode = 'r+' if os.path.isfile(filename) else 'w+'
        self._file = open(filename, mode)

        if not root:
            parsed = parse(self._file)
            self._root = parsed if parsed != None else JsonObject()
        else:
            self._root = root

        self.d = JsonDotNotation(self._root)

    def __len__(self):
        return self._root.__len__()

    def __delitem__(self, key):
        return self._root.__delitem__(key)

    def __getitem__(self, key):
        return self._root.__getitem__(key)

    def _format_str(self):
        unformat_str = self._root.__str__()
        tabs = 0
        space = ' ' * 4
        for line in unformat_str.split('\n'):
            open_br = re.search(r'[\}\]],?\s*$', line)
            close_br = re.search(r'[\{\[]\s*$', line)
            op_cl_br = re.search(r'(?:{\s*}|\[\s*\]),?\s*$', line)

            if open_br and not op_cl_br:
                tabs -= 1
            yield space * tabs + line
            
            if close_br:
                tabs += 1

    def __str__(self):
        return '\n'.join(self._format_str())

    def __repr__(self):
        return self._root.__repr__()

    def __setitem__(self, key, value):
        return self._root.__setitem__(key, value)

    def __getattr__(self, attrname):
        return self._root.__getattribute__(attrname)

    def tree_copy(self):
        return copy.deepcopy(self._root)

    def clear(self, new_root=JsonObject()):
        self._root = new_root
        self.d = JsonDotNotation(self._root)

    def close(self):
        self._file.seek(0)
        self._file.truncate()
        self._file.writelines(self.__str__())
        self._file.close()
