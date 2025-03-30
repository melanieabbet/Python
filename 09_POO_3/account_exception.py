class NotEnoughMoneyException(Exception):
    def __init__(self, message):
        self.message = message

class OwnerError(ValueError):
    def __init__(self, message):
        self.message = message