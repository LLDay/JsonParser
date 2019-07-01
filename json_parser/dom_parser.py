from .token import *
from .json_tree import JsonTreeBuilder

class TokenRules:
    def open_object(tree, tok):
        tree.add_object()

    def add_key(tree, tok):
        tree.add_key(tok.get_content(1))

    def close_object(tree, tok):
        tree.back()

    def open_list(tree, tok):
        tree.add_list()

    def close_list(tree, tok):
        tree.back()

    def add_string(tree, tok):
        tree.add_value(tok.get_content(1))

    def add_digit(tree, tok):
        tree.add_value(float(tok.get_content(1)))

    def add_tfn(tree, tok):
        tree.add_value(tok.get_content(1))


def parse():
    json_builder = JsonTreeBuilder()

    rules = {
        TokenType.OpenObject: TokenRules.open_object,
        TokenType.CloseObject: TokenRules.close_object,
        TokenType.Key: TokenRules.add_key,
        TokenType.OpenList: TokenRules.open_list,
        TokenType.CloseList: TokenRules.close_object,
        TokenType.ValueTFN: TokenRules.add_tfn,
        TokenType.ValueString: TokenRules.add_string,
        TokenType.ValueDigit: TokenRules.add_digit
    }

    for token in get_tokens('test.json'):
        rules.get(token.get_type(), lambda tree, tok: 0)(json_builder, token)
    
    print(json_builder.get_tree())
