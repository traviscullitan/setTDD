class setTDD():

    def __init__(self):
        self.data = {}
    
    def __len__(self):
        return len(self.data)
    
    def append(self, value):
        self.data[value] = True
    
    def remove(self, value):
        if value in self.data:
            del self.data[value]
        else:
            raise ValueError("No Such Element In Set")

