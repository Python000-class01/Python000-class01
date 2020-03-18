from abc import ABCMeta, abstractmethod
from typing import Optional, List, Union
from decimal import Decimal


class Goods:
    name = ''
    price = Decimal()

    def __str__(self):
        return f'goods:{self.name}'

    def __repr__(self):
        return f'goods:{self.name}'


class Apple(Goods):
    name = 'apple'
    price = Decimal('11.1111')


class Orange(Goods):
    name = 'orange'
    price = Decimal('23.34111')


class User(metaclass=ABCMeta):
    discount_method = []

    def __init__(self, money: Union[int, float, Decimal] = 0, quantity: int = 0, cart: Optional[List[Goods]] = None):
        self.money = Decimal(str(money))
        self.quantity = quantity
        self.shopping_cart = cart or list()

    def __call__(self, *args, **kwargs):
        return self.pay()

    def pay(self) -> Decimal:
        pay_money = self.money
        for method in self.discount_method:
            pay_money = min(method(self)(), pay_money)

        print(f'{self.__class__.__name__} money:{self.money} quantity:{self.quantity} pay_money {pay_money}')
        return pay_money

    def add(self, goods: Goods, num: int = 1) -> None:
        for i in range(num):
            self.shopping_cart.append(goods)
            self.money += goods.price
            self.quantity += 1

    def clear(self) -> None:
        self.money = 0
        self.quantity = 0
        self.shopping_cart = list()


class Discount(metaclass=ABCMeta):
    def __call__(self, *args, **kwargs):
        return self.pay()

    def __init__(self, user: User):
        self.user = user

    @abstractmethod
    def pay(self):
        pass


class NormalDiscount(Discount):
    def pay(self):
        if self.user.money >= 200:
            return Decimal('0.9') * self.user.money
        return self.user.money


class VipDiscount1(Discount):
    def pay(self):
        if self.user.money >= 200:
            return Decimal('0.8') * self.user.money
        return self.user.money


class VipDiscount2(Discount):
    def pay(self):
        if self.user.quantity >= 10:
            return Decimal('0.85') * self.user.money
        return self.user.money


class NormalUser(User):
    discount_method = [NormalDiscount]


class VipUser(User):
    discount_method = [VipDiscount1, VipDiscount2]


if __name__ == '__main__':
    NormalUser(100, 1)()
    NormalUser(200, 1)()
    NormalUser(300, 1)()
    NormalUser(400, 1)()

    VipUser(100, 1)()
    VipUser(200, 1)()
    VipUser(300, 1)()
    VipUser(400, 1)()
    VipUser(100, 10)()
    VipUser(200, 10)()
    VipUser(300, 10)()
    VipUser(400, 10)()

    apple = Apple()
    a = NormalUser()
    a.add(apple, 100)
    print(a.shopping_cart)
    print(len(a.shopping_cart))
    a.pay()

    b = VipUser()
    b.add(apple, 50)
    print(len(b.shopping_cart))
    b.pay()
