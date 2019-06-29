from .token import Token
from .lex_tree import LexTreeBuilder

def get_json_tree(filename):
    lex_tree = LexTreeBuilder()

    key = Token('key', r'\"(.*)\":')
    opo = Token('opo', r'\{')
    clo = Token('clo', r'\}')
    opl = Token('opl', r'\[')
    cll = Token('cll', r'\]')
    sep = Token('sep', r',')
    val = Token(
        'val', r'(?:\"(.*)\"|(-?[\d]+(?:.[\d]+)?)|(true|false|null))')
    
    beg = Token('beg', r'')
    end = Token('end', r'')
    
    beg.expects([opo, opl])
    key.expects([val, opo, opl])
    opo.expects([key, clo, opl])
    clo.expects([sep, clo, cll, end])
    opl.expects([val, cll, opo])
    cll.expects([sep, cll, clo, end])
    sep.expects([key, val, opo, opl])
    val.expects([sep, cll, clo])

    file = open(filename)
    all_json = file.read()
    file.close()

    yield beg
    last_token = beg

    while last_token != end:
        last_json = all_json

        for token in last_token:
            if all_json in token:
                all_json = all_json[len(token.get_content()):]
                token_founded = True
                last_token = token
                yield token
                break

        if token != end and all_json == last_json:
            raise RuntimeError

