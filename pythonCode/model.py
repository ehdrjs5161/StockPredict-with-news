

class model:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.result = None

    def getcode(self):
        return self.code

    def setcode(self, code):
        self.code = code
