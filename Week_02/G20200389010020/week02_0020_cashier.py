class Account(object):

    def __init__(self, orders):
        self.totalNumber = sum([order[0] for order in orders])
        self.totalPrice = sum([order[0] * order[1] for order in orders])


class AccountNormal(Account):

    def pay(self):
        if self.totalPrice < 200:
            return self.totalPrice
        else:
            return self.totalPrice * 0.9


class AccountVip(Account):

    def pay(self):
        if self.totalPrice >= 200:
            price1 = self.totalPrice * 0.8
        else:
            price1 = self.totalPrice

        if self.totalNumber >= 10:
            price2 = self.totalPrice * 0.85
        else:
            price2 = self.totalPrice

        if price1 > price2:
            return price2
        else:
            return price1


if __name__ == '__main__':
    orders1 = [
        [2, 200],
        [1, 30],
    ]
    orders2 = [
        [20, 1],
        [1, 30],
    ]

    print(AccountNormal(orders1).pay())
    print(AccountVip(orders1).pay())

    print(AccountNormal(orders2).pay())
    print(AccountVip(orders2).pay())
