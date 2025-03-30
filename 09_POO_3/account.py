from account_exception import NotEnoughMoneyException
class Account:
    ''' Simple représentation d'un compte bancaire 

    >>> a = Account("Melanie", 200, "CHF")
    >>> a[0]
    200
    >>> a.deposit(200)
    >>> a[0]
    400
    '''
    def __init__(self, owner,balance,currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency
        self.history =[self.balance]

    def display(self):
        print(f"Le solde du compte de Paul est de {self.balance} {self.currency}")
    def deposit(self, value):
        if value > 0:
            self.balance += value
            self.history.insert(0, self.balance)
        else:
            raise ValueError("Un dépot doit être un chiffre positif")
    def withdraw(self, value):
        if value >= 0:
            if self.balance - value > 0:
                self.balance -= value
                self.history.insert(0, self.balance)
            else:
                raise NotEnoughMoneyException("Not enought money available")
        else:
            raise ValueError("Votre valeur de retrait doit être un chiffre positif")
    def __getitem__(self,index):
        try:
            return self.history[index]
        except IndexError:
            raise(IndexError('Not enough transactions'))

        
if __name__ == '__main__':
    import doctest
    doctest.testmod()