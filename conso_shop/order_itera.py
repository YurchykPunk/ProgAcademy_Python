class OrderIterator:

    def __init__(self, container):
        self.container_p = container[0]
        self.container_q = container[1]
        self.index = 0
        
    def __next__(self):
        if self.index < len(self.container_p):
            self.index += 1
            return (self.container_p[self.index - 1], self.container_q[self.index - 1])
        else:
            raise StopIteration
        
    def __iter__(self):
        return self