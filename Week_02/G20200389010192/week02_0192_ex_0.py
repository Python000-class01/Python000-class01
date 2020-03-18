class Member(object):

    def __init__(self, role):
        self.vip = role


class SettleAccount(Member):

    def __init__(self, price, cases, role):
        self.price = price
        self.cases = cases
        Member.__init__(self, role)

    def discount(self):
        if self.vip is True:
            if self.price >= 200:
                self.price = self.price * 0.8
            else:
                if self.cases >= 10:
                    self.price = self.price * 0.85
        else:
            if self.price >= 200:
                self.price = self.price * 0.9


a = SettleAccount(100, 5, False)
a.discount()
print(a.price)

b = SettleAccount(400, 5, True)
b.discount()
print(b.price)

c = SettleAccount(100, 12, True)
c.discount()
print(c.price)