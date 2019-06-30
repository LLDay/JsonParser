from .token import *
from .lex_tree import LexTreeBuilder

def get_tokens(filename):
    key = TokenGen(TokenType.Key, r'\"(.*)\":')
    opo = TokenGen(TokenType.OpenObject, r'\{')
    clo = TokenGen(TokenType.CloseObject, r'\}')
    opl = TokenGen(TokenType.OpenList, r'\[')
    cll = TokenGen(TokenType.CloseList, r'\]')
    sep = TokenGen(TokenType.Separator, r',')
    val = TokenGen(TokenType.Value, r'(?:\"(.*)\"|(-?[\d]+(?:.[\d]+)?)|(true|false|null))')
    
    beg = TokenGen('beg', r'')
    
    beg.expects([opo, opl])
    key.expects([val, opo, opl])
    opo.expects([key, clo, opl])
    clo.expects([sep, clo, cll])
    opl.expects([val, cll, opo])
    cll.expects([sep, cll, clo])
    sep.expects([key, val, opo, opl])
    val.expects([sep, cll, clo])

    file = open(filename)
    all_text = file.read()
    file.close()

    last_gen = beg

    tok_list = [key, opo, clo, opl, cll, sep, val]
    while all_text:
        last_json = all_text

        for tokenGen in last_gen.expectation_list():
            token = tokenGen.generate(all_text)
            if token:
                all_text = all_text[len(token.get_content()):]
                last_gen = tokenGen
                yield token
                break

        if all_text == last_json:
            raise RuntimeError

