from enum import Enum
from .json_components import JsonList, JsonObject


class JsonTreeBuilder:
    '''
    Provides methods for generate JSON tree step by step

    Functions call order matters
    '''

    def __init__(self): 
        self._root        = None
        self._current     = None
        self._pointer_key = None
        self._trace = []

    def add_key(self, key_name):
        '''
        Add a key inside the object

        { "`key_name`": ... }
        '''
        if not isinstance(self._current, dict):
            raise RuntimeError("Only objects may have keys")

        if key_name in self._current:
            raise RuntimeError("A key must be unique within an object")
        self._pointer_key = key_name


    def _into(self):
        self._trace.append(self._current)
        if isinstance(self._current, list):
            self._current = self._current[-1]

        elif isinstance(self._current, dict):
            self._current = self._current[self._pointer_key]

        else:
            raise RuntimeError('Unspecified object: ' + str(self._trace.pop()))


    def _add_any_value(self, value):
        if isinstance(self._current, list):
            self._current.append(value)

        elif isinstance(self._current, dict):
            self._current[self._pointer_key] = value

        else:
            raise RuntimeError('Unspecified object: ' + str(self._current))


    def add_object(self):
        '''
        Adds a new object to the last key / list / object

        "last_key" : { }
        '''
        if self._root == None:
            self._root = JsonObject()
            self._current = self._root
            self._trace.append(self._current)
            return

        self._add_any_value(JsonObject())
        self._into()


    def add_list(self):
        '''
        Adds a new list to the last key / list / object

        "last_key" : [ ]
        '''
        if self._root == None:
            self._root = JsonList()
            self._current = self._root
            self._trace.append(self._current)
            return

        self._add_any_value(JsonList())
        self._into()


    def add_value(self, value):
        '''
        Inits key by `value` or adds values to the last list 

        "last_key" : `value`;
        "last_key" : [..., `value`]
        '''
        self._add_any_value(value)
        

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
