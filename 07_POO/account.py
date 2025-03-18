class Account:
    ''' Simple représentation d'un compte bancaire '''
    def __init__(self, owner,balance,currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency
    def display(self):
        print(f"Le solde du compte de Paul est de {self.balance} {self.currency}")
    def deposit(self, value):
        if value > 0:
            self.balance += value
        else:
            raise ValueError("Un dépot doit être un chiffre positif")
    def withdraw(self, value):
        if value >= 0:
            if self.balance - value > 0:
                self.balance -= value
            else:
                raise Exception("Not enought money available")
        else:
            raise ValueError("Votre valeur de retrait doit être un chiffre positif")