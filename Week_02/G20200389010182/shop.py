
'''
普通用户消费不足 200 元，无折扣，原价付费；
普通用户消费满 200 元打九折；
VIP 会员满 200 元打八折；
VIP 会员满 10 件商品打八五折。
'''

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer','name vip')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0.0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}'
        return fmt.format(self.total(), self.due())

class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        '''return discount value'''

# 总价打折
class TotalPricePromotion(Promotion):
    def discount(self, order):
        if ( order.customer.vip == 1) :
            return order.total() * 0.2 if order.total() >= 200 else 0.0
        else:
            return order.total() * 0.1 if order.total() >= 200 else 0.0


# 商品数量超过10打折
class BulkItemPromotion(Promotion):
    def discount(self, order):
        if order.customer.vip:
            distinct_items = {item.quantity for item in order.cart}
            if sum(distinct_items) >= 10:
                return order.total() * 0.15
            return 0
        return 0

# e.g,
joe = Customer('John Doe', 0)
# vip
ann = Customer('Ann Smith', 1)

# < 200
cart1 = [LineItem('banana', 2, 8),
        LineItem('apple', 9, 7),
        LineItem('watermelon', 5, 20)]
# Order(joe, cart1,TotalPricePromotion())
# Order(ann, cart1,TotalPricePromotion())

# > 200
cart2 = [LineItem('banana', 8, 8.0),
        LineItem('apple', 9, 6.0),
        LineItem('watermelon', 5, 20)]
# Order(joe, cart2,TotalPricePromotion())
# Order(ann, cart2,TotalPricePromotion())

# > 200 and item > 10
cart3 = [LineItem('banana', 8, 8),
        LineItem('apple', 10, 6),
        LineItem('watermelon', 5, 20)]
# Order(ann, cart3,TotalPricePromotion())
# Order(ann, cart3, BulkItemPromotion())

# return cheapest for vip
customer_vip = ann
cart_vip     = cart2
promos = [TotalPricePromotion, BulkItemPromotion]
min_total = 1000000
for promo in promos:
    promo_total = Order(customer_vip, cart_vip, promo()).total()
    if promo_total < min_total:
        min_total = promo_total 
        class_name = promo

def best_promo(order):
    return max(promo(order) for promo in promos)