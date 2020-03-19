# 为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分
# 并按照不同的购买金额、不同的用户身份进行结账：
#
# 普通用户消费不足 200 元，无折扣，原价付费；
# 普通用户消费满 200 元打九折；
# VIP 会员满 200 元打八折；
# VIP 会员满 10 件商品打八五折。
# 要求：
# 请使用面向对象编程实现结算功能。
# 由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。
class Customer(object):
    def __init__(self,level,money,count):
        self.level = level
        self.money = money
        self.count = count

    def levels(self):
        return Vip(self.money, self.count) if self.level == 'vip' else Nonvip(self.money, self.count)


class Pay(object):
    def __init__(self):
        self.money = money

    def discount_no(self):
        print(f" money ¥{self.money:.2f}")

    def discount_09(self):
        print(f" money ¥{self.money *0.9:.2f}")

    def discount_08(self):
        print(f" money ¥{self.money * 0.8:.2f}")

    def discount_085(self):
        print(f" money ¥{self.money * 0.85:.2f}")

class Nonvip(Customer,Pay):
    def __init__(self, money, count):
        self.money = money
        self.count = count


    @property
    def shop(self):
            return self.discount_no() if self.money < 200  else self.discount_09()

class Vip(Customer,Pay):
    def __init__(self, money, count):
        self.count = count
        self.money = money

    @property
    def shop(self):
        if self.money >= 200:
            return self.discount_08()
        elif self.money < 200 and self.count >= 10:
            return self.discount_085()
        else:
            return self.discount_no()

if __name__ == '__main__':
    ss = Customer('vip', 200, 11).levels()
    ss.shop
