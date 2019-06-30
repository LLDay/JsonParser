class TreeNode:
    def __init__(self, val, val_type):
        self._val = val
        self._type = val_type

    def is_list(self):
        return self._type == 'list'

    def is_object(self):
        return self._type == 'object'

    def is_single(self):
        return self._type == 'single'

    

class LexTreeBuilder:
    def __init__(self):
        self._root = {}
        self._current = self._root
        self._trace = []

    def add_object(self, key_name):
        self._current[key_name] = {}
        self._trace.append(self._current)
        self._current = self._current[key_name]

    def add_value(self, key, value):
        self._current[key] = value

    def back(self):
        self._current = _trace.pop()

    def start(self):
        self._current = self._root
        self._trace = []

    def to(self, key):
        start()

        for k in key.split('.'):
            self._trace.append(self._current)
            self._current = self._current[k]
