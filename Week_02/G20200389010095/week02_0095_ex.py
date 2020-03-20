#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Consunmer(object):
    type_consunmer= 0# 0:common  1:vip
    money = 0
    count = 0

    def __init__(self, type_consunmer, money, count):
        self.type_consunmer = type_consunmer
        self.money = money
        self.count = count

class Balance(object):

    def juge_type_consumer(self, consumer:Consunmer)-> float:
        if consumer.type_consunmer == 1:
            return self.vip_consumer(consumer)
        return self.common_consumer(consumer)

    def common_consumer(self, consumer:Consunmer)-> float:
        money = consumer.money
        if money <= 0:
            return 0
        if money >= 200:
            return money*0.9
        return money

    def vip_consumer(self, consumer:Consunmer)-> float:
        money = consumer.money
        count = consumer.count
        if money <= 0:
            return 0
        if money >= 200:
            return money*0.8
        if count >= 10:
            return money*0.85
        return money



# 0:common  1:vip
if __name__=='__main__':
    common = Consunmer(0,200,4)
    vip = Consunmer(1,200,10)
    balance = Balance()
    print("消费共计：%d" %(balance.juge_type_consumer(common)))
    print("消费共计：%d" %(balance.juge_type_consumer(vip)))
