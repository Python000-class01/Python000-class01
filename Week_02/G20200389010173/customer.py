

class Customer(object):
    account = 1000
    type = 'normal'
    def __init__(self, account, type):
        self.account = account
        self.type = type
    def pay(self, money):
        self.account = self.account - money
