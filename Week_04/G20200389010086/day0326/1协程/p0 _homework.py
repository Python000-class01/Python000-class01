#!/usr/bin/env python
#coding: utf-8

class BasePromotion(object):

    """
    折扣策略类
    """

    def __call__(self, order):
        pass

class NormalPromotion(BasePromotion):
    """
    折扣策略类，没有折扣
    """

    def __call__(self, order):
        return order.total

class RebatePromotion(BasePromotion):
    """
    折扣策略类，满减
    """

    def __init__(self, money=0, discount=1):

        self.money = money
        self.discount = discount

    def __call__(self, order):

        return order.total if order.total < self.money else order.total * self.discount

class CountRebatePay(BasePromotion):
    """
    折扣策略类，满多少件减
    """

    def __init__(self, count=1, discount=1):

        self.count = count
        self.discount = discount

    def __call__(self, order):

        return order.total if order.count < self.count else order.total * self.discount


class Customer(object):
    """
    消费者
    """

    def __init__(self, name, vip):
        self.name = name
        self.vip = vip

class Item(object):

    """
    商品
    """

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def total(self):
        return self.price * self.count

class Order(object):
    """
    订单
    """

    def __init__(self, customer, cart, promotions=[NormalPromotion()]):
        self.customer = customer
        self.cart = cart
        self.promotions = promotions

        self.__total = 0
        self.__count = 0

    @property
    def total(self):
        if self.__total:
            return self.__total
        self.__total = sum(i.total() for i in self.cart)
        return self.__total

    @property
    def count(self):
        if self.__count:
            return self.__count
        self.__count = sum(i.count for i in self.cart)
        return self.__count

    def due(self):
        return min(p(self) for p in self.promotions)

class Pay(object):
    """
    支付
    """

    def __init__(self, customer, cart):

        self.customer = customer
        self.cart = cart

    def __call__(self):
        if self.customer.vip:
            order = Order(self.customer, self.cart, promotions=vip_promotions)
        else:
            order = Order(self.customer, self.cart, promotions=promotions)
        return order.due()

if __name__ =='__main__':

    # 定义各种折扣
    p_90 = RebatePromotion(200, 0.9)
    p_80 = RebatePromotion(200, 0.8)
    p_10_85 = CountRebatePay(10, 0.85)
    
    # 定义折扣形式分组列表
    promotions = [p_90]
    vip_promotions = [p_80, p_10_85]

    # 消费者
    c = Customer('User1', True)
    # 购物车
    cart = [
        Item('milk', 10, 1),
        Item('apple', 1, 10),
        Item('t01', 10, 10),
        Item('t02', 1, 10),
        Item('t03', 1, 10),
        Item('t04', 1, 10),
        Item('t05', 1, 10),
        Item('t06', 1, 10),
        Item('t07', 1, 10),
        Item('t08', 1, 10),
        Item('t09', 1, 10),
    ]

    # 支付
    p = Pay(c, cart)
    print(p())
