    

class JsonTreeBuilder:
    def __init__(self):
        self._root = {}
        self._current = self._root
        self._trace = []


    def add_key(self, key_name):
        pass

    def add_object(self):
        pass

    def add_list(self):
        pass

    def add_value(self, value):
        pass


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
