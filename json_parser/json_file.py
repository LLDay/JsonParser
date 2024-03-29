import re
import os.path
import copy

from .dom_parser import parse
from .json_components import *


class JsonFile:
    def __init__(self, filename, root=None):
        if os.path.isfile(filename):
            self._file = open(filename, 'r+')
        else:
            self._file = None
            self._filename = filename

        if root == None:
            self._root = parse(self._file) if self._file else JsonObject()
        else:
            self._root = root

        self.d = JsonDotNotation(self._root)

    def __len__(self):
        return self._root.__len__()

    def __delitem__(self, key):
        return self._root.__delitem__(key)

    def __getitem__(self, key):
        return self._root.__getitem__(key)

    def __contains__(self, key):
        return self._root.__contains__(key)

    def _format_str(self, spaces_number):
        unformat_str = self._root.__str__()
        tabs = 0
        space = ' ' * spaces_number
        res = []

        for line in unformat_str.split('\n'):
            close_brackets = re.search(r'(?<![\{\[])[\}\]],?$', line)
            if close_brackets:
                tabs -= 1

            res.append(space * tabs + line)

            open_brackets = re.search(r'[\{\[]\s*$', line)
            if open_brackets:
                tabs += 1            

        return '\n'.join(res)

    def __str__(self):
        return self._format_str(4)

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

    def save(self, spaces_number=4):
        if self._file == None:
            self._file = open(self._filename, 'w')
        self._file.seek(0)
        self._file.truncate()
        self._file.writelines(self._format_str(spaces_number))
        return self

    def close(self):
        if self._file != None:
            self._file.close()
