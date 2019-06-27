import re


class LexTree:
    def __init__(self):
        self.root = {}
        self.current = root
        self.trace = []

    def add_object(self, key_name):
        self.current[key_name] = {}
        self.trace.append(self.current)
        self.current = self.current[key_name]

    def add_value(self, key, value):
        self.current[key] = value

    def back(self):
        self.current = trace.pop()

    def start(self):
        self.current = self.root
        self.trace = []

    def to(self, key):
        start()

        for k in key.split('.'):
            self.trace.append(self.current)
            self.current = self.current[k]


class Token:
    def __init__(self, name, regex):
        self.name = name
        self.regex = r'[ \n\t]*' + regex
        self.expects = []

    def set_line(self, line):
        self.result = re.match(self.regex, line)

    def __bool__(self):
        if result:
            return True
        else:
            return False

    def get_content(self, groupName):
        return self.result.group(groupName)

    def expects(self, tokens):
        self.expects.append(tokens)


def get_json_tree(filename):
    key = Token('key', r'\"(?<string>.*)\"[\n\t ]*:')
    opo = Token('opo', r'\{')
    clo = Token('clo', r'\}')
    opl = Token('opl', r'\[')
    cll = Token('cll', r'\]')
    sep = Token('sep', r',')
    val = Token(
        'val', r'\"(?<string>.*)\"|(?<digit>-?[\d]+(?:.[\d]+)?)|(?<value>true|false|null)')
    nth = Token('nth', r'')

    key.expects([val, opo, opl])
    opo.expects([key, clo])
    clo.expects([sep, nth, clo])
    opl.expects([key, cll])
    cll.expects([sep, clo])
    sep.expects([key, val])
    val.expects([sep, cll, clo])
