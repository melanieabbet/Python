from account_exception import NotEnoughMoneyException, OwnerError
class Account:
    ''' Simple représentation d'un compte bancaire 

    >>> a = Account("Melanie", 200, "CHF")
    >>> a[0]
    200
    >>> a.deposit(200)
    >>> a[0]
    400
    '''
    _accounts ={}
    def __init__(self, owner,balance,currency):

        if owner in Account._accounts:
            raise OwnerError(f"{owner} alread owns an account!")
        self.owner = owner
        self.balance = balance
        self.currency = currency
        self.history =[self.balance]
        Account._accounts[owner] = self 

    def display(self):
        print(f"Le solde du compte de {self.owner} est de {self.balance} {self.currency}")
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
    @classmethod
    def from_owner(cls,owner):
        account = cls._accounts.get(owner)
        if account:
            return account
        else:
            raise OwnerError(f"No account found for {owner}")
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()