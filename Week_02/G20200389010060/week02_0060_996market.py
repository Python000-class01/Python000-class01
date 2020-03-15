# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 下午7:56
# @Author  : Mat
# @Email   : ZHOUZHENZHU406@pingan.com.cn
# @File    : 996market.py

from collections.abc import Iterable
from abc import abstractmethod


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f'id:{self.id},name:{self.name},price{self.price}'

class Discount:
    @abstractmethod
    def get_discounted_total_price(self, product_num, total_price) -> int:
        pass


class Normal200BillDiscount(Discount):
    # 重载get_discounted_total_price函数
    def get_discounted_total_price(self, product_num, total_price) -> int:
        return total_price * 0.9 if total_price >= 200 else total_price


class Vip200BillDiscount(Discount):
    # 重载get_discounted_total_price函数
    def get_discounted_total_price(self, product_num, total_price) -> int:
        return total_price * 0.8 if total_price >= 200 else total_price

class Vip10ProductsDiscount(Discount):
    def get_discounted_total_price(self, product_num, total_price) -> int:
        return total_price * 0.85 if product_num >= 10 else total_price


def vip_wrapper(cls):
    class inner(cls):
        def __init__(self,name):
            self.name=name
            super().__init__()
            self.add_discount_method(Vip200BillDiscount())
            self.add_discount_method(Vip10ProductsDiscount())
    return inner


def normal_wrapper(cls):
    class inner(cls):
        def __init__(self,name):
            self.name = name
            super().__init__()
            self.add_discount_method(Normal200BillDiscount())
    return inner


class Customer:
    def __init__(self):
        self.products = []
        self.prices=[]
        self.goods=[]
        self.__discount_methods = []

    def add_discount_method(self, func):
        self.__discount_methods.append(func)

    def buy_product(self, products):
        if isinstance(products, Iterable):
            self.products.extend(products)
        else:
            self.products.append(products)

    def pay_bill(self):
        self.prices = [x.price for x in self.products]
        print(f'self.prices:{self.prices}')
        self.goods=[x.name for x in self.products]
        print(f'self.goods:{self.goods}')
        product_num, total_price = len(self.products), sum([x.price for x in self.products])
        final_price=total_price
        for discount in self.__discount_methods:
            final_price = min(final_price, discount.get_discounted_total_price(product_num, total_price))
        print(f'Customer payed {final_price} for products:\n{self.products}')
        self.products = []

@vip_wrapper
class VipCustomer(Customer):
    pass

@normal_wrapper
class NormalCustomer(Customer):
    pass

if __name__ == '__main__':
    normalcustomer = NormalCustomer('Normal')
    vipcustomer = VipCustomer('Vip')

    #普通用户满200打9折
    normalcustomer.buy_product([Product(f'id{i}', f'product{i}', 100) for i in range(4)])
    normalcustomer.pay_bill()

    #普通用户不打折
    normalcustomer.buy_product([Product(f'id{i}', f'product{i}', 25) for i in range(4)])
    normalcustomer.pay_bill()

    # vip用户满200打8折
    vipcustomer.buy_product([Product(f'id{i}', f'product{i}', 100) for i in range(4)])
    vipcustomer.pay_bill()

    # vip用户满10件打85折
    vipcustomer.buy_product([Product(f'id{i}', f'product{i}', 10) for i in range(10)])
    vipcustomer.pay_bill()

    # vip用户同时满足满10件和满200元，选最多折扣8折
    vipcustomer.buy_product([Product(f'id{i}', f'product{i}', 20) for i in range(10)])
    vipcustomer.pay_bill()

    # vip用户不打折
    vipcustomer.buy_product([Product(f'id{i}', f'product{i}', 25) for i in range(4)])
    vipcustomer.pay_bill()