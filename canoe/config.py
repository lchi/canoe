class Config(object):
    pass

class PythonConfig(Config):
    def __init__(self, m):
        self.mod = __import__(m)

    def get_canoe(self):
        return self.mod.Canoe(["apple", "pie"])
