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
    def __init__(self, name, regex, content_group = 0):
        self.name = name
        self.regex = r'[ \n\t]*' + regex
        self.last_size = 0
        self.content_group = content_group

    def __contains__(self, line):
        result = re.match(self.regex)
        if result:
            self.last_size = len(result.group(0))
            return True
        else:
            return False

    def get_content(self, line):
        return re.match(self.regex).group(self.content_group)

def get_json_tree(filename):
    key = Token('key', r'\"(.*)\"[\n\t ]*:', 1)
    opo = Token('opo', r'\{')
    clo = Token('clo', r'\}')
    opl = Token('opl', r'\[')
    cll = Token('cll', r'\]')
    sep = Token('sep', r',') 

