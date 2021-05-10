# This is my solution to this kata: https://www.codewars.com/kata/5a03af9606d5b65ff7000009/train/python

class User(object):
    '''A class managing some operations done by a bank client.
    \nArguments: name, balance, and checking_account (boolean).'''
    def __init__(self, name, balance, checking_account,*args,**kwargs):
        self.name = name.lower().capitalize()
        self.balance = balance
        self.checking_account = checking_account
        self.__dict__.update(**kwargs)
    def withdraw(self, money):
        ''' Withdraws money from balance'''
        self.money = money
        if self.money <= self.balance:
            self.balance -= self.money
            return f'{self.name} has {self.balance}.'
        else:
            raise ValueError('Not enough money.')
    def check(self, other_user, money):
        '''Getting paid by check from other_user'''
        if other_user.checking_account is False or other_user.balance < money: # I wrote "is" because it is a boolean, not any value that returns False (== works too)
            raise ValueError('This operation is impossible.')
        other_user.balance -= money
        self.balance += money
        return f'{self.name} has {self.balance} and {other_user.name} has {other_user.balance}.' 
    def add_cash(self,money):
        '''Adds money to balance'''
        self.money = money
        self.balance += self.money
        return f'{self.name} has {self.balance}.'

# Now demonstrating inheritance 

class Superuser(User):
    '''If a user belongs to this class inherited from the User class, then everything is possible to her/him!'''
    power = 'almighty'
    def __init(self, *args, **kwargs): # any optional args and keyword args are accepted
        super().__init__(*args, **kwargs) #super() is used to inherit the attributes of User (name, balance, checking_account)