class Customer(object):

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


one = Customer('Rakesh',1000)
print(one.withdraw(50))
print(one.deposit(600))
