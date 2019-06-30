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
        return self._type.name

    def __repr__(self):
        return "Token('{0}', '{1}')".format(self.get_content(), self._type.name)


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

    def expectations(self):
        return self._expects

    def generate(self, text):
        content = re.match(self._lexem, text)
        return Token(content, self._type)

    def __str__(self):
        return self._type

    def __repr__(self):
        return "TokenGen('{0}')".format(self._lexem)

def get_token_generator():
    key = TokenGen(TokenType.Key, r'\"(.*)\":')
    opo = TokenGen(TokenType.OpenObject, r'\{')
    clo = TokenGen(TokenType.CloseObject, r'\}')
    opl = TokenGen(TokenType.OpenList, r'\[')
    cll = TokenGen(TokenType.CloseList, r'\]')
    sep = TokenGen(TokenType.Separator, r',')
    val = TokenGen(TokenType.Value,
                   r'(?:\"(.*)\"|(-?[\d]+(?:.[\d]+)?)|(true|false|null))')
    beg = TokenGen(TokenType.Begin, r'')

    beg.expects([opo, opl])
    key.expects([val, opo, opl])
    opo.expects([key, clo, opl])
    clo.expects([sep, clo, cll])
    opl.expects([val, cll, opo])
    cll.expects([sep, cll, clo])
    sep.expects([key, val, opo, opl])
    val.expects([sep, cll, clo])

    return beg

def get_tokens(filename):
    with open(filename) as file:
        last_gen = get_token_generator()
        text = ' '

        while True:
            last_read = file.readline()
            text += last_read
            found_token = True

            while found_token:
                if not text.strip():
                    break
                
                found_token = False

                for tokenGen in last_gen.expectations():
                    token = tokenGen.generate(text)

                    if token:
                        text = text[len(token.get_content()):]
                        last_gen = tokenGen
                        found_token = True
                        yield token
                        break

            if text and not last_read:
                raise RuntimeError
            
            if not text and not last_read:
                break
