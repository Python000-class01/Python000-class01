
# 996便利店
class Customer(object):
    # 静态字段
    # 商品列表
    good_list = []
    # 数量
    total_quantity = 0
    # 总额
    total = 0
    # 结算金额
    amount = 0

    def __init__(self, is_vip = False):
        # 普通字段
        self.vip = is_vip

    def buy(self, good_name, quantity, price):
        self.total_quantity = self.total_quantity + quantity
        self.total = self.total + quantity*price
        good = {}
        good[good_name] = {'quantity':quantity, 'price':price}
        self.good_list.append(good)

    def __pay_for_normal(self):
        if self.total >= 200:
            self.amount = self.total * 0.9
        else:
            self.amount = self.total

        return self.amount

    def __pay_for_vip(self):
        # 条件1
        if self.total >= 200:
            amount1 = self.total * 0.8
        else:
            amount1 = self.total
        # 条件2
        if self.total_quantity >= 10:
            amount2 = self.total * 0.85
        else:
            amount2 = self.total
        # 哪个更优惠付哪个钱
        self.amount =  amount1 if amount1 < amount2 else amount2

        return self.amount

    def pay(self):
        if self.vip:
            amount = self.__pay_for_vip()
        else:
            amount = self.__pay_for_normal()

        return amount


normal = Customer()
normal.buy('西瓜', 3, 2)
normal.buy('车厘子', 1, 50)
normal.buy('榴莲', 2, 80)
print(normal.pay())


vip = Customer(True)
vip.buy('笔', 10, 2)
vip.buy('书包', 1, 200)
print(vip.pay())

