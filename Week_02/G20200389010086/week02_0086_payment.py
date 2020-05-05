class Custom(object):
    total_money = 0  # 商品总价格
    total_goods = 0  # 商品总数

    def __init__(self, name, user_type, goods=None):
        self.name = name
        self.user_type = user_type  # 用户类型（0 ：普通用户  1：vip）
        if goods is None:
            goods = []
        self.goods = goods

    def buy(self, *args):
        self.goods.append(*args)

    def pay(self):
        for items in self.goods:
            for item in items:
                self.total_money += item[1] * item[2]
                self.total_goods += item[2]

        self.total_money = float('%2f' % self.total_money)

        # 普通用户结算
        if self.user_type == 0:
            OrdinaryObj = OrdinaryPay(self.name, self.user_type)
            OrdinaryObj.pays(self.total_money)
        # vip 结算
        if self.user_type == 1:
            VipObj = VipsPay(self.name, self.user_type)
            VipObj.pays(self.total_money, self.total_goods)


# vip 付款计算折扣
class VipsPay(Custom):
    def pays(self, total_money, total_goods):

        payment_amount = 0
        if total_money < 200 and total_goods >= 10:
            payment_amount = total_money * 0.85

        if total_money < 200 and total_goods < 10:
            payment_amount = total_money

        if total_money >= 200:
            payment_amount = total_money * 0.8

        print(f'顾客{self.name}，你好：你需要支付{payment_amount: .2f}元')


# 普通用户计算折扣
class OrdinaryPay(Custom):
    def pays(self, total_money):
        payment_amount = 0
        if total_money < 200:
            payment_amount = total_money

        if total_money >= 200:
            payment_amount = total_money * 0.9

        print(f'顾客{self.name},你好：你需要支付{payment_amount: .2f}元')


# 执行入口
# 商品参数  商品名、单价、数量
if __name__ == '__main__':
    CustomObj = Custom('张三', 0)
    CustomObj.buy([['Apple', 5.3, 6], ['Banana', 4.2, 4]])
    CustomObj.pay()
