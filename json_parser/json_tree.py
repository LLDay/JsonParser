from enum import Enum

class JsonValues(Enum):
    null = 0
    true = 1
    false = 2

class JsonTreeBuilder:
    '''
    Provides methods for generate JSON tree step by step

    Functions call order matters
    '''

    def __init__(self):
        self._root = {}
        self._current = self._root
        self._trace = []
        self._pointer_key = 'root'


    def add_key(self, key_name):
        '''
        Add a key inside the object

        { "`key_name`": ... }
        '''
        self._pointer_key = key_name

    def add_object(self):
        '''
        Adds a new object to the last key / list / object

        "last_key" : { }
        '''
        self._trace.append(self._current)
        if isinstance(self._current, list):
            self._current.append({})
            self._current = self._current[-1]
        else:
            self._current[self._pointer_key] = {}
            self._current = self._current[self._pointer_key]

    def add_list(self):
        '''
        Adds a new list to the last key / list / object

        "last_key" : [ ]
        '''
        self._trace.append(self._current)
        if isinstance(self._current, list):
            self._current.append([])
            self._current = self._current[-1]
        else:
            self._current[self._pointer_key] = []
            self._current = self._current[self._pointer_key]

    def add_value(self, value):
        '''
        Inits key by `value` or adds values to the last list 

        "last_key" : `value`;
        "last_key" : [..., `value`]
        '''
        if isinstance(self._current, list):
            self._current.append(value)
        else:
            self._current[self._pointer_key] = value

    def get_tree(self):
        '''
        Returns built tree
        '''
        if self._current != self._root:
            raise RuntimeError('Json has errors')
        return self._root

    def back(self):
        '''
        Ends a work with the object / list

        Returns to the level above
        '''
        self._current = self._trace.pop()
