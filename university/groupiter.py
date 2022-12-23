

class GroupIterative:
    def __init__(self, container):
        self.container = container
        self.index = 0

    def __next__(self):
        if self.index < len(self.container):
            self.index += 1
            return self.container[self.index - 1]
        else:
            raise StopIteration
    
    def __iter__(self):
        return self