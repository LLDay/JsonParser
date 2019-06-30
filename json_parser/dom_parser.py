from .token import TokenGen
from .lex_tree import LexTreeBuilder

def get_json_tree(filename):
    key = TokenGen(r'\"(.*)\":')
    opo = TokenGen(r'\{')
    clo = TokenGen(r'\}')
    opl = TokenGen(r'\[')
    cll = TokenGen(r'\]')
    sep = TokenGen(r',')
    val = TokenGen(r'(?:\"(.*)\"|(-?[\d]+(?:.[\d]+)?)|(true|false|null))')
    
    beg = TokenGen(r'')
    end = TokenGen(r'')
    
    beg.expects([opo, opl])
    key.expects([val, opo, opl])
    opo.expects([key, clo, opl])
    clo.expects([sep, clo, cll])
    opl.expects([val, cll, opo])
    cll.expects([sep, cll, clo])
    sep.expects([key, val, opo, opl])
    val.expects([sep, cll, clo])

    file = open(filename)
    all_json = file.read()
    file.close()

    yield beg
    last_token = beg

    while all_json:
        last_json = all_json

        for tokenGen in last_token.expectation_list():
            token = tokenGen.generator(all_json)
            if token:
                all_json = all_json[len(token.get_content()):]
                last_token = token
                yield token
                break

        if all_json == last_json:
            raise RuntimeError

    yield end
