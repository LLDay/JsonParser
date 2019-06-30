import re
from enum import Enum

class Token:
    def __init__(self, content, token_type):
        self._type = token_type
        self._content = content

    def __bool__(self):
        return self._content != None

    def get_content(self, group=0):
        return self._content.group(group)

    def __str__(self):
        return self._type

    def __repr__(self):
        return "Token('{0}', '{1}')".format(self.get_content(), self._type)


class TokenType(Enum):
    Key = 0
    OpenObject = 1
    CloseObject = 2
    OpenList = 3
    CloseList = 4
    Separator = 5
    Value = 6
    Begin = 7


class TokenGen:
    def __init__(self, token_type, lexem):
        self._type = token_type
        self._lexem = r'[ \n\t]*' + lexem
        self._expects = []

    def expects(self, tokens):
        self._expects.extend(tokens)

    def expectation_list(self):
        return self._expects

    def generate(self, line):
        content = re.match(self._lexem, line)
        return Token(content, self._type)

    def __str__(self):
        return self._type

    def __repr__(self):
        return "TokenGen('{0}')".format(self._lexem)
