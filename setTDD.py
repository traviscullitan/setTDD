class setTDD():

    def __init__(self):
        self.data = {}
    
    def __len__(self):
        return len(self.data)
    
    def append(self, value):
        self.data[value] = True

