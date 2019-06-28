from .token import Token

def get_json_tree(filename):
    key = Token('key', r'\"(.*)\"[\n\t ]*:')
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
    
    json_tokens = [beg]

    file = open(filename)
    all_json = file.read()
    file.close()

    while json_tokens[-1] != end:
        last_token = json_tokens[-1]
        last_json = all_json

        for token in last_token:
            if all_json in token:
                json_tokens.append(token)
                all_json = all_json[len(token.get_content()):]
                token_founded = True
                break

        if token != end and all_json == last_json:
            raise RuntimeError

    return json_tokens

