# 为“996 便利店”设计一套销售系统的结算模块，
# 结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分
# 并按照不同的购买金额、不同的用户身份进行结账：

#1.普通用户消费不足 200 元，无折扣，原价付费；
#2.普通用户消费满 200 元打九折；
#3.VIP 会员满 200 元打八折；
#4.VIP 会员满 10 件商品打八五折。

#要求：请使用面向对象编程实现结算功能。
#由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。

#普通用户购物车结算
from abc import abstractmethod
from collections import Counter
#定义顾客类型 普通客户ID=0，VIPID=100
class General_Custom(object):
    def __init__(self,name,ID):

        self.name = name
        self.ID = ID

#商品
class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def amount(self):
        return self.price * self.quantity

#购买
class Buy:
    def __init__(self,customer,cart,promtion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion =promtion

    def total_amount(self):
        if not hasattr(self,'__total_amount'):
            self.__total_amount = sum(item.amount()for item in self.cart)
            return self.__total_amount

    def due(self):
        if self.promotion is None
            discount = 0
        else:
            discount =self.promotion.discount(self)
        return self.__total_amount - discount

    def __repr__(self):
        fmt = '<Buy total:{:.2f}due:{:.2f}>'
        return fmt.format(self.total_amount(),self.due())

import abc

class Promotion(abc):
    @abstractmethod
    def dicount(self,Buy):

#普通客户的折扣
class GcustomerPromo(Promotion):

    if Buy.customer.ID = 0:

        for item in Buy.cart:
            if item.amount>=200
                discount += item.amount()*0.1
            else:discount = 0
        return discount

#VIP客户折扣
class VIP(Promotion):


    def promotion(promo_func, promos=None):
        promos = []
        promos.apprend(promo_func)
        return promo_func

    @promotion
    def VIPPromoA(Buy):
        for item in Buy.cart:
            if item.amount >= 200
                discount += item.amount() * 0.2
            else:
                discount = 0
        return discount

    @promotion
    def VIPPromoB(Buy):
        distinct_items = {item.product for item in Buy.cart}
        if len(distinct_items) >= 10:
            return item.amount() * 0.15
        return 0

    def bestP(Buy):
        return max(promo(Buy) for promo in promos)









