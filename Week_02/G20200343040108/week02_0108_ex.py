# -*- encoding=utf-8 -*-
# @File: week02_0108_ex.py
# @Author：wsr
# @Date ：2020/3/17 15:24

# 普通用户消费不足 200 元，无折扣，原价付费；
# 普通用户消费满 200 元打九折；
# VIP 会员满 200 元打八折；
# VIP 会员满 10 件商品打八五折。
# 要求：
# 请使用面向对象编程实现结算功能。
# 由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。

class Shop996():
    # 满 200 元价格条件
    amount_limit = 200

    # 满 10 条件
    num_limit = 10

    # 根据价格打折： 1 普通用户 九折； vip用户 八折
    discount_amounts = {1: 0.9, 2: 0.8}

    # 根据件数打折：1 普通用户（无折扣）; 2 vip用户， 满10件八五折
    discount_nums = {1: 1, 2: 0.85}

    # 价格列表
    price_list = {'book': 15, 'phone': 90, 'cup': 80}

    def __init__(self, username, goods=None):
        self.username = username
        if goods == None:
            goods = []
        self.goods = goods

    # 购买物品
    def buy(self, goods_name, goods_num=1):
        item = {
            'goods_name': goods_name,
            'goods_num': goods_num
        }
        self.goods.append(item)

    # 结账
    def pay_up(self):
        print("username: ", self.username)
        total_price = 0
        total_nums = 0
        for good in self.goods:
            price = self.price_list[good['goods_name']] * good['goods_num']
            print("goods: %s, num: %d, total_money: %s" % (good['goods_name'], good['goods_num'], price))
            total_price += price
            total_nums += good['goods_num']

        print("username: %s 总共花了 %s " % (self.username, total_price))


# vip 用户
class VipUser(Shop996):
    # 结账
    def pay_up(self):
        print("username: ", self.username)
        total_price = 0
        total_nums = 0
        for good in self.goods:
            price = self.price_list[good['goods_name']] * good['goods_num']
            print("goods: %s, num: %d, total_money: %s" % (good['goods_name'], good['goods_num'], price))
            total_price += price
            total_nums += good['goods_num']

        total_price1 = total_price2 = total_price
        # 根据 vip 会员满200打八折
        if total_price > self.amount_limit:
            total_price1 = total_price * self.discount_amounts[2]

        # 根据 vip 会员满10件打八五折
        if total_nums > self.num_limit:
            total_price2 = total_price * self.discount_nums[2]

        if total_price1 > total_price2:
            total_price_new = total_price2
        else:
            total_price_new = total_price1

        print("username: %s 总共花了 %s, 优惠后的价格为：%s" % (self.username, total_price, total_price_new))


# 普通用户
class CommonUser(Shop996):
    # 结账
    def pay_up(self):
        print("username: ", self.username)
        total_price = 0
        total_nums = 0
        for good in self.goods:
            price = self.price_list[good['goods_name']] * good['goods_num']
            print("goods: %s, num: %d, total_money: %s" % (good['goods_name'], good['goods_num'], price))
            total_price += price
            total_nums += good['goods_num']

        total_price_new = total_price
        # 根据 vip 会员满200打八折
        if total_price > self.amount_limit:
            total_price_new = total_price * self.discount_amounts[1]

        print("username: %s 总共花了 %s, 优惠后的价格为：%s" % (self.username, total_price, total_price_new))


# shop1 = Shop996('test')
# shop1.buy('book',10)
# shop1.pay_up()
#
# shop2 = Shop996('tom')
# shop2.buy('book',5)
# shop2.pay_up()

print("vip用户")
vip1 = VipUser('test')
vip1.buy('book', 3)
vip1.buy('phone', 1)
vip1.pay_up()

vip2 = VipUser('test2')
vip2.buy('book', 30)
vip2.buy('phone', 3)
vip2.pay_up()

print("\n普通用户")
common1 = CommonUser('tom')
common1.buy('book', 21)
common1.pay_up()

common2 = CommonUser('tom2')
common2.buy('cup', 2)
common2.buy('book', 1)
common2.pay_up()
