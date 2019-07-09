from .token import TokenType, get_tokens
from .json_builder import JsonTreeBuilder


class TokenRules:
    def add_key(tree, tok):
        tree.add_key(tok.get_content(1))

    def open_object(tree, tok):
        tree.add_object()

    def close_object(tree, tok):
        tree.back()

    def open_list(tree, tok):
        tree.add_list()

    def close_list(tree, tok):
        tree.back()

    def add_string(tree, tok):
        tree.add_value(tok.get_content(1))

    def add_digit(tree, tok):
        digit = tok.get_content(1)
        if '.' in digit:
            tree.add_value(float(digit))
        else:
            tree.add_value(int(digit))

    def add_tfn(tree, tok):
        value = {
            'true'  : True,
            'false' : False,
            'null'  : None
        }[tok.get_content(1)]
        
        tree.add_value(value)


def parse(filename):
    json_builder = JsonTreeBuilder()

    rules = {
        TokenType.OpenObject  : TokenRules.open_object,
        TokenType.CloseObject : TokenRules.close_object,
        TokenType.Key         : TokenRules.add_key,
        TokenType.OpenList    : TokenRules.open_list,
        TokenType.CloseList   : TokenRules.close_object,
        TokenType.ValueTFN    : TokenRules.add_tfn,
        TokenType.ValueString : TokenRules.add_string,
        TokenType.ValueDigit  : TokenRules.add_digit
    }

    for token in get_tokens(filename):
        rules.get(token.get_type(), lambda tree,
                  tok: None)(json_builder, token)

    return json_builder.get_tree()
