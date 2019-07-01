from . import dom_parser as dp

class JsonParser(dict):
    def __init__(self, filename):
        return super().__init__(dp.parse(filename))

    def __getitem__(self, key):
        return super().__getitem__('root')[key]

    def __setitem__(self, key, value):
        return super().__getitem__('root').__setitem__(key, value)

    def __len__(self):
        return super().__getitem__('root').__len__()

    def get(self, key, default=None):
        return super()._getitem__('root').get(key, default)
    

    # def close(self):
    #     pass
