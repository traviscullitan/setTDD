class setTDD():

    def __init__(self):
        self.data = {}
        self.iter_data = None
    
    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        self.iter_data = iter(self.data)
        return self
    
    def __next__(self):
        return next(self.iter_data)

    def append(self, value):
        self.data[value] = True
    
    def remove(self, value):
        if value in self.data:
            del self.data[value]
        else:
            raise ValueError("No Such Element In Set")

