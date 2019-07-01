

class JsonTreeBuilder:
    def __init__(self):
        self._root = {}
        self._current = self._root
        self._trace = []
        self._pointer_key = 'root'


    def add_key(self, key_name):
        self._pointer_key = key_name

    def add_object(self):
        self._trace.append(self._current)
        if isinstance(self._current, list):
            self._current.append({})
            self._current = self._current[-1]
        else:
            self._current[self._pointer_key] = {}
            self._current = self._current[self._pointer_key]

    def add_list(self):
        self._trace.append(self._current)
        if isinstance(self._current, list):
            self._current.append([])
            self._current = self._current[-1]
        else:
            self._current[self._pointer_key] = []
            self._current = self._current[self._pointer_key]

    def add_value(self, value):
        if isinstance(self._current, list):
            self._current.append(value)
        else:
            self._current[self._pointer_key] = value

    def get_tree(self):
        if self._current != self._root:
            raise RuntimeError('Json has errors')
        return self._root

    def back(self):
        self._current = self._trace.pop()

    def start(self):
        self._current = self._root
        self._trace = []


    def to(self, key):
        start()

        for k in key.split('.'):
            self._trace.append(self._current)
            self._current = self._current[k]
