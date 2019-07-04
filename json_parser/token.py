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

    def get_type(self):
        return self._type

    def __str__(self):
        return self._type.name


class TokenType(Enum):
    Key         = 0
    OpenObject  = 1
    CloseObject = 2
    OpenList    = 3
    CloseList   = 4
    Separator   = 5
    ValueString = 6
    ValueDigit  = 7
    ValueTFN    = 8
    Begin       = 9
    Root        = 10



class TokenGen:
    def __init__(self, token_type, lexem):
        self._type = token_type
        self._lexem = r'\s*' + lexem
        self._expects = []

    def expects(self, token):
        if isinstance(token, list):
            self._expects.extend(token)
        else:
            self._expects.append(token)

    def expectations(self):
        return self._expects

    def generate(self, text):
        content = re.match(self._lexem, text)
        return Token(content, self._type)

    def __str__(self):
        return self._type


def _get_token_generator():
    key = TokenGen(TokenType.Key, r'\"(.*)\":')
    opo = TokenGen(TokenType.OpenObject, r'\{')
    clo = TokenGen(TokenType.CloseObject, r'\}')
    opl = TokenGen(TokenType.OpenList, r'\[')
    cll = TokenGen(TokenType.CloseList, r'\]')
    sep = TokenGen(TokenType.Separator, r',')
    vst = TokenGen(TokenType.ValueString, r'\"(.*)\"')
    vdi = TokenGen(TokenType.ValueDigit, r'(-?\d+(?:.\d+)?(?:[eE][-+]?\d+)?)')
    vbn = TokenGen(TokenType.ValueTFN, r'(true|false|null)')
    beg = TokenGen(TokenType.Begin, r'')

    beg.expects([opo, opl])
    key.expects([vst, vdi, vbn, opo, opl])
    opo.expects([key, clo, opl])
    clo.expects([sep, clo, cll])
    opl.expects([vst, vdi, vbn, cll, opo])
    cll.expects([sep, cll, clo])
    sep.expects([key, vst, vdi, vbn, opo, opl])
    vst.expects([sep, cll, clo])
    vdi.expects([sep, cll, clo])
    vbn.expects([sep, cll, clo])

    return beg



def get_tokens(filename):
    with open(filename) as file:
        last_gen = _get_token_generator()
        text = ''

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
