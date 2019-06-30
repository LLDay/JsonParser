import re

class Token:
    def __init__(self, content, functor=None):
        self._content = content
        self._functor = functor

    def __bool__(self):
        return self._content.__bool__()

    def get_content(self, group=0):
        return self._content.group(group)


class TokenGen:
    def __init__(self, lexem):
        self._lexem = r'[ \n\t]*' + lexem
        self._expects = []
        self._result = ''
        self._behavior = lambda: 0

    def expects(self, tokens):
        self._expects.extend(tokens)

    def expectation_list(self):
        return self._expects

    def generate(self, line):
        return Token(re.match(self._lexem, line), self._behavior)

    def __repr__(self):
        return "TokenGen('{0}')".format(self._lexem)
