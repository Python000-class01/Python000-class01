#!usr/bin/env
#-*- coding:utf -8-*-

class Customer(object):
    #父类
    def __init__(self, name, money, goods=None):
        self.name = name
        self.money = float(money)
        if goods is None:
            goods = []
        self.goods = goods

    def account(self):
        count = len(self.goods)
        print("您一共买了{} 件商品，共消费: {} 元".format(count, self.money))

class NormalCustomer(Customer):
    #普通用户
    def account(self):
        if self.money < 200:
            print("您一共消费：{} 元".format(self.money))
        else:
            print("您所买商品打九折，一共消费：{} 元".format(self.money*0.9))

class VipCustomer(Customer):
    #vip用户
    def account(self):
        count = len(self.goods)
        if count == 0 and self.money == 0:
            print("您没有消费")
        if self.money >= 200:
            print("您一共买了{} 件商品，总价打八折，共消费: {} 元".format(count, self.money*0.8))
        elif count >= 10 and self.money < 200:
            print("您一共买了{} 件商品，总价打八五折，共消费: {} 元".format(count, self.money*0.85))
        elif count < 10:
            print("您一共买了{} 件商品，共消费: {} 元".format(count, self.money))


normal_cus = NormalCustomer("Amy", 190)
normal_cus.account()
vip_cus0 = VipCustomer("Kate", 0)
vip_cus0.account()
vip_cus1 = VipCustomer("Kate", 300, ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
vip_cus1.account()
vip_cus2 = VipCustomer("Kate", 200, ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
vip_cus2.account()

#结果输出
# 您一共消费：190.0 元
# 您没有消费
# 您一共买了0 件商品，共消费: 0.0 元
# 您一共买了10 件商品，总价打八折，共消费: 240.0 元
# 您一共买了9 件商品，总价打八折，共消费: 160.0 元
