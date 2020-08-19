class basicLogFile():
    def __init__(self, path):
        self.path = path

    def addEntry(self, strIn):
        with open(self.path, 'a') as file:
            file.write(strIn)

    def reset(self):
        with open(self.path, 'w') as file:
            file.write('')