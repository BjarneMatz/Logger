class Logger:
    def __init__(self):
        self.debugging = False
    def print(self, logmessage):
        if self.debugging:
            print(logmessage)
    def enable(self):
        self.debugging = True
    def disable(self):
        self.debugging = False