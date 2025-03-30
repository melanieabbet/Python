class Multiples:
    def __init__(self, number, limit=float('inf')):
        self.number = number
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self
    
    def __next__(self):
        self.current += self.number
        if self.current < self.limit:
            return self.current
        else:
            raise StopIteration
