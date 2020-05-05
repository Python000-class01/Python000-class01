# store 模块
# import math


"""
1⃣️为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：

普通用户消费不足 200 元，无折扣，原价付费；
普通用户消费满 200 元打九折；
VIP 会员满 200 元打八折；
VIP 会员满 10 件商品打八五折。
要求：
请使用面向对象编程实现结算功能。
由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。

"""


class User(object):
    # type 0-normal 1-vip
    def __init__(self, user_type, amount, goods_count=0):
        self.user_type = user_type
        self.amount = amount
        self.goods_count = goods_count


def get_normal_user_settlement(amount):
    if amount < 200:
        return amount
    else:
        return 0.9 * amount


def get_vip_user_settlement(amount, goods_count):
    amount_settlement = 0.85 * amount if goods_count >= 10 else amount
    goods_count_settlement = 0.8 * amount if amount >= 200 else amount
    return min(amount_settlement, goods_count_settlement)


def settlement(user_type, amount, goods_count):
    if user_type == 0:
        return get_normal_user_settlement(amount)
    elif user_type == 1:
        return get_vip_user_settlement(amount, goods_count)


if __name__ == '__main__':
    u1 = User(0, 100)
    u2 = User(0, 200)

    v1 = User(1, 100, 6)
    v2 = User(1, 100, 15)

    v3 = User(1, 300, 6)
    v4 = User(1, 300, 15)

    users = {u1, u2, v1, v2, v3, v4}

    for u in users:
        name = 'normal user' if u.user_type == 0 else 'vip user'
        print(
            f'{name} 原始金额 {u.amount} ¥,购买 {u.goods_count} 件商品，结算后金额 {settlement(u.user_type, u.amount, u.goods_count)}')
