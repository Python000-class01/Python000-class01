#!/usr/bin/env python
import random

class Goods(object):
    goods = {}

    @classmethod
    def load(cls, name, price, number):
        cls.goods[name] = (price, number)

def goodsload():
    # 上货
    # Goods.load('商品名称', '单价', '数量')
    Goods.load('茄子', '1.9', 1000)
    Goods.load('豆角', '2.9', 1000)
    Goods.load('白菜', '2.9', 1000)
    Goods.load('山药', '18.9', 1000)
    Goods.load('菠萝', '20.9', 1000)
    Goods.load('车厘子', '99', 1000)
    Goods.load('土豆', '3.99', 1000)
    Goods.load('西红柿', '4.99', 1000)
    Goods.load('萝卜', '9.99', 1000)
    Goods.load('芹菜', '10.99', 1000)
    Goods.load('胡萝卜', '11.99', 1000)
    print(Goods.goods)                  # 货架商品


class Person(object):
    def __init__(self):
        if 'shoppingList' not in locals().keys(): shoppingList = {}
        self.shoppingList = shoppingList    # 购物清单
        self.prices = 0         # 商品价值
        self.payPrices = 0      # 支付价值
        self.discount = 0.9     # 折扣系数
    def shopping(self, goods, number):
        """加购物车"""
        if goods in Goods.goods:
            self.shoppingList[goods] = (Goods.goods[goods][0], number)
        else:
            print(f'{goods} 无货')
    def pay(self):
        """结账"""
        self.prices = sum([float(v[0])*float(v[1]) for k,v in self.shoppingList.items()])
        self.discount = self.discount if self.prices >= 200 else 1
        self.payPrices = self.prices * self.discount
        return f'{self.payPrices:0.2f}'
    def __str__(self):
        # return f'{self.role}, {self.payPrices}, {self.shoppingList}'
        return f'{self.role}, {self.payPrices:0.2f}(折扣价) | {self.prices:0.2f}(共消费) * {self.discount}(折扣) | 购物清单{self.shoppingList}'

class Customer(Person):
    def __init__(self):
        self.role = 'normal'
        super().__init__()

class Vip(Person):
    def __init__(self):
        self.role = 'vip'
        super().__init__()
    def pay(self):
        """结账"""
        self.prices = sum([float(v[0])*float(v[1]) for k,v in self.shoppingList.items()])
        # self.discount = (self.discount-0.05) if self.prices >= 200 else 1
        self.discount = 0.85 if len(self.shoppingList) >= 10 else 1
        self.discount = 0.8 if self.prices >= 200 else self.discount
        self.payPrices = self.prices * self.discount


if __name__ == "__main__":
    # 上货
    goodsload()

    # tom 普通消费者，购物不满 200，不打折
    tom = Customer()
    tom.shopping('茄子', 2)
    tom.shopping('豆角', 4)
    tom.pay()
    print(f'tom:', tom)

    # jim 普通消费者，购物满 200，9 折
    jim = Customer()
    jim.shopping('茄子', 200)
    jim.shopping('豆角', 40)
    jim.pay()
    print(f'jim:', jim)

    # mike vip用户，购物满 200，8 折
    mike = Vip()
    mike.shopping('茄子', 200)
    mike.shopping('豆角', 40)
    mike.pay()
    print(f'mike:', mike)

    # kate vip 满 10 件不满 200， 85 折
    kate = Vip()
    for g in Goods.goods:
        kate.shopping(g, 1)
    kate.pay()
    print(f'kate:', kate)

    # kate vip 满 10 件，满 200，8 折
    bill = Vip()
    for g in Goods.goods:
        bill.shopping(g, 10)
    bill.pay()
    print(f'bill:', bill)