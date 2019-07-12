from .dom_parser import parse
from .json_objects import *

class JsonFile:
    def __init__(self, filename, base=JsonObject):
        self._file = open(filename)
        self._root = parse(self._file)
        self._base = base
        self.d = JsonDotNotation(self._root)

        if not self._root:
            self_root = self._base.copy()

    def __len__(self):
        return self._root.__len__()

    def __getitem__(self, key):
        return self._root.__getitem__(key)

    def __setitem__(self, key, value):
        return self._root.__setitem__(key, value)

    def __getattr__(self, attrname):
        return self._root.__getattribute__(attrname)

    def close(self):
        self._file.close()
