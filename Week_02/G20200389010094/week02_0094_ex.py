'''
为"996便利店"设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：

    普通用户消费不足 200 元，无折扣，原价付费；
    普通用户消费满 200 元打九折；
    VIP 会员满 200 元打八折；
    VIP 会员满 10 件商品打八五折。
    要求：
    请使用面向对象编程实现结算功能。
    由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


DATA_LIST = [
    [36, 41, 37, 20, 45, 20, 14, 8, 49, 6, 46, 13, 3, 31, 16, 3, 10, 14],
    [48, 3, 11, 49, 19, 25, 31, 38, 33, 4, 6, 8, 3, 5, 30, 40, 2, 14],
    [13, 43, 16, 42, 38, 35, 42],
    [16, 20, 31, 6, 34, 17, 12, 22, 39, 46, 6, 13, 35, 3, 42],
    [9, 37, 31, 31, 19, 13, 46, 47, 36, 27, 14, 6, 12, 48, 33, 20, 2, 19, 33],
    [4, 40, 6, 27, 1, 41, 36, 22, 15, 7, 44],
    [15, 21, 31, 27, 17, 27, 26, 41, 34, 34, 43, 7, 32, 41, 25, 22, 8, 33],
    [5, 22, 41, 13, 35, 41, 47, 30, 36, 8, 48, 31],
    [2, 32, 46, 28, 16, 21, 13],
    [48, 46, 35, 1, 31, 22],
    [31, 18, 36, 8, 3, 35, 37, 26, 21, 13, 7, 9],
    [38, 42, 32, 35, 16],
    [35, 20, 11, 21, 6, 11, 33],
    [16, 7, 41, 23, 43, 13, 18, 42, 48, 24, 20, 46, 42, 12, 7],
    [7, 49, 13, 45, 38, 15, 38, 40, 20, 9, 12, 8, 31, 17],
    [42, 36, 38, 15, 10, 32, 35, 34, 16, 6, 1],
    [21, 40, 26, 40, 36, 34, 24, 8, 40, 33],
    [16, 41, 25, 25, 43, 40, 38, 49, 14, 18, 8, 26],
    [21, 43, 33, 4, 4, 37, 10, 49, 5, 17, 46, 27, 46, 12, 28, 29, 38, 39],
    [46, 7, 14, 46, 43, 39, 41, 31, 42, 21, 17, 30, 38, 13]
]


class Customer(object):
    ''' Customer '''
    def __init__(self):
        self.__cnt = 0
        self.__total = 0.0

    def bill(self):
        pay_total = self.__total
        if pay_total > 200:
            pay_total *= 0.9
        print(f'总共消费{pay_total:.1f}元')

    def shopping(self, menu=None):
        assert isinstance(menu, list)
        self.__total = math.fsum(menu)
        self.__cnt += len(menu)

    def clean(self):
        self.__cnt = 0
        self.__total = 0.0


class CustomerVIP(object):
    '''VIP'''
    def __init__(self):
        self.__cnt = 0
        self.__total = 0.0

    def bill(self):
        pay_total = 0
        sum0 = sum1 = self.__total
        if self.__cnt > 10:
            sum0 = self.__total * 0.85
        if self.__total > 200:
            sum1 = self.__total * 0.8
        if sum0 < sum1:
            pay_total = sum0
        else:
            pay_total = sum1
        print(f'总共消费{pay_total:.1f}元')

    def shopping(self, menu=None):
        assert isinstance(menu, list)
        self.__total = math.fsum(menu)
        self.__cnt += len(menu)

    def clean(self):
        self.__cnt = 0
        self.__total = 0.0


def customer_aaa():
    '''a common customer'''
    person_a = Customer()
    for i in DATA_LIST:
        person_a.shopping(i)
        person_a.bill()
        person_a.clean()

def customer_bbb():
    '''a VIP customer'''
    person_b = CustomerVIP()
    for i in DATA_LIST:
        person_b.shopping(i)
        person_b.bill()
        person_b.clean()


if __name__ == '__main__':
    print('---------------------------------')
    customer_aaa()
    print('---------------------------------')
    customer_bbb()
    print('---------------------------------')
