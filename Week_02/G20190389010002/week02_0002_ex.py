#!/bin/env python
# encoding=utf-8

import sys

goods_list = dict(苹果=100, 矿泉水=150, 饮料=200, 香烟=100, 面包=120, 哇哈哈=300, 大碗面=400, 康师傅=100, 酸酸乳=120)

class Custom(object):

    def __init__(self, customer_type, goods=None):
        """
        :param customer_type: 1 vip，2 普通
        :param goods:
        """
        self.customer_type = customer_type
        if goods is None:
            goods = {}
        self.goods = goods

    def buy(self):
        if self.customer_type == '1':
            self.vip_pay_up()
        if self.customer_type == '2':
            self.custom_pay_up()

    def vip_pay_up(self):
        # 结账
        account = 0
        for item in self.goods:
            sales = goods_list[item]
            account = account + sales

        if account >= 200:
            print('共计消费:', account * 0.8, '元，折扣8折')
        elif len(goods_list) >= 10:
            print('共计消费:', account * 0.85, '元，折扣85折')
        else:
            print('共计消费:', account, '元')

    def custom_pay_up(self):
        # 结账
        account = 0
        for item in self.goods:
            sales = goods_list[item]
            account = account + sales
        if account < 200:
            print('共计消费:', account, '元')
        if account >= 200:
            print('共计消费:', account * 0.9, '元，折扣9折')


if __name__ == '__main__':

    message = print('Please choice vip or customer.')
    #选择会员还是普通客户
    inform = 'vip'

    if inform == 'vip':
        custom1 = Custom('1', goods_list)
        custom1.buy()
    if inform == 'customer':
        customer2 = Custom('2', goods_list)
        customer2.buy()