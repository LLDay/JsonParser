import re

class Token:
    def __init__(self, lex_type, lexem):
        self._type = lex_type
        self._lexem = r'[ \n\t]*' + lexem
        self._expects = []
        self._result = ''
        self._behavior = lambda: 0

    def get_content(self, grouplex_type=0):
        return self._result.group(grouplex_type)

    def expects(self, tokens):
        self._expects.extend(tokens)


    def behavior(self, f):
        self._behavior = f

    def do(self):
        self._behavior()


    def __contains__(self, line):
        self._result = re.match(self._lexem, line)
        if self._result:
            return True
        else:
            return False

    def __bool__(self):
        if self._result:
            return True
        else:
            return False


    def __iter__(self):
        return self._expects.__iter__()

    def __str__(self):
        return self._type

    def __repr__(self):
        return 'Token(\'{0}\', \'{1}\')'.format(self._type, self._lexem)
