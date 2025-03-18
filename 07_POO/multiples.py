class Multiples:
    def __init__(self, number):
        self.number = number
        self._original_number = number
    def next(self):
        self.number += self._original_number
        return self.number 
