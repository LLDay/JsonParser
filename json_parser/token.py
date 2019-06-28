import re

class Token:
    def __init__(self, name, regex):
        self._name = name
        self._regex = r'[ \n\t]*' + regex
        self._expects = []
        self._result = ''

    def __contains__(self, line):
        self._result = re.match(self._regex, line)
        if self._result:
            return True
        else:
            return False

    def __bool__(self):
        if self._result:
            return True
        else:
            return False

    def get_content(self, groupName=0):
        return self._result.group(groupName)

    def expects(self, tokens):
        self._expects.extend(tokens)

    def __iter__(self):
        return self._expects.__iter__()

    def __str__(self):
        return self._name

    def __repr__(self):
        return 'Token(\'{0}\', \'{1}\')'.format(self._name, self._regex)
