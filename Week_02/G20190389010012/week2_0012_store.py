#!/usr/local/bin/python3
"""
作业一：
为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：
1.普通用户消费不足 200 元，无折扣，原价付费；
2.普通用户消费满 200 元打九折；
3.VIP 会员满 200 元打八折；
4.VIP 会员满 10 件商品打八五折。
要求：
1.请使用面向对象编程实现结算功能。
2.由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。
"""


class Customer:
    """
    消费类
    """

    def __init__(self, vip, amount, num=0):
        self.vip = vip
        self.amount = amount
        self.num = num

    @staticmethod
    def _vip_pay(amount, num):
        """
        vip结算
        :param int amount: 消费金额
        :param int num: 产品数量
        :return: amount 结算价格
        """
        if amount >= 200:
            return amount * 0.8
        elif amount < 200 and num >= 10:
            return amount * 0.85
        else:
            return amount

    @staticmethod
    def _normal_pay(amount):
        """
        正常结算
        :param int  amount: 商品金额
        :return:
        """
        if amount >= 200:
            return amount * 0.9
        return amount

    def pay(self):
        """
        支付
        :return:
        """
        if self.vip:
            return self._vip_pay(self.amount, self.num)
        else:
            return self._normal_pay(self.amount)


if __name__ == '__main__':
    customer = Customer(vip=True, amount=199, num=9)
    print("VIP结算价格：%s" % customer.pay())
    customer = Customer(vip=False, amount=200)
    print("普通用户结算价格：%s" % customer.pay())
