    

class LexTreeBuilder:
    def __init__(self):
        self._root = {}
        self._current = self._root
        self._trace = []

    def add_object(self):
        self._current[key_name] = {}
        self._trace.append(self._current)

    def add_value(self, value):
        self._current.append(value)

    def add_key(self, key_name):
        self._current[key_name] = []
        self._trace.append(_current)
        self._current = self._current[key_name]

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
