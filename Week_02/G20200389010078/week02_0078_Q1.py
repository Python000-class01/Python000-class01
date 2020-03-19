# 为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：

# 普通用户消费不足 200 元，无折扣，原价付费；
# 普通用户消费满 200 元打九折；
# VIP 会员满 200 元打八折；
# VIP 会员满 10 件商品打八五折。
# 要求：

# 请使用面向对象编程实现结算功能。
# 由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。

class Customers(object):
    # 顾客的父类
    def __init__(self, name, goods=None, price=None, amount=None):
        self.name = name
        if goods is None:
            goods = []
        self.goods = goods
        if price is None:
            price = []
        self.price = price
        if amount is None:
            amount = []
        self.amount = amount

    def buy(self, goods_name, goods_price, goods_amount):
        # 购买物品
        self.goods.append(goods_name)
        self.price.append(goods_price)
        self.amount.append(goods_amount)

    def shopping_list(self):
        # 顾客姓名与购物清单(包含单价和数量)
        print(self.name)
        print([item for item in self.goods])
        print([item for item in self.price])
        print([item for item in self.amount])


class Normal_Customers(Customers):
    # 顾客父类的子类普通客户
    def pay_up(self):
        # 普通用户结账
        payment_due = 0
        final_payment = 0
        l = len(self.goods)
        for i in range(l):
            payment_due += self.price[i] * self.amount[i]
        if payment_due < 200:
            final_payment = payment_due
        else:
            final_payment = payment_due * 0.9
        print(f"亲爱的顾客{self.name}，您需要支付{final_payment}元")


class VIP_Customers(Customers):
    # 顾客父类的子类普通客户
    def pay_up(self):
        # 普通用户结账
        final_payment = 0
        payment_due = 0
        l = len(self.goods)
        for i in range(l):
            payment_due += self.price[i] * self.amount[i]
        if sum(self.amount) >= 10 and payment_due < 200:
            final_payment = payment_due * 0.85
        elif payment_due >= 200:
            final_payment = payment_due * 0.8
        elif sum(self.amount) < 10 and payment_due < 200:
            final_payment = payment_due
        print(f"亲爱的会员{self.name}，您需要支付{final_payment}元")


custom1 = VIP_Customers('tom')
custom1.buy('apple', 1, 1.5)
custom1.buy('banana', 2, 3)

custom2 = Normal_Customers('jerry')
custom2.buy('cake', 5, 1)
custom1.shopping_list()
print(custom1.pay_up())
custom2.shopping_list()
print(custom2.pay_up())
