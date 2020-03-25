# 顾客结束购物
class Shopping(object):
    def __init__(self, items, total):
        self.items = items
        self.total = total
        print(f'本次您一共购买了{self.items}件商品，原价合计{self.total}元')


# 普通会员结账
class Normal(Shopping):

    def __init__(self, items, total):
        super().__init__(items, total)

    def discount(self):
        print('您是本店普通会员，购物满200可享受9折优惠')
        if self.total < 200:
            _subtotal = self.total
            print('您本次购物金额未满200元')
        else:
            _subtotal = self.total * 0.90
        return _subtotal


# VIP会员结账
class Vip(Shopping):

    def __init__(self, items, total):
        super().__init__(items, total)

    def discount(self):
        print('您是本店VIP会员，购物满10件享受85折优惠，购物满200元享受8折优惠')
        if self.total < 200 and self.items < 10:
            _subtotal = self.total
            print('本次购物您未满足优惠条件')
        elif self.total < 200 and self.items >= 10:
            _subtotal = self.total * 0.85
            print('本次购物满10件，总金额不满200元，按照85折优惠')
        elif self.total >= 200:
            _subtotal = self.total * 0.8
            print('本次总金额满200元，按照8折优惠')
        return _subtotal


# 收银
class Cash_register():

    @staticmethod
    def checkout(membership, items, total):
        print('欢迎光临996便利店！')
        if membership == 'normal':
            subtotal = Normal(items, total).discount()
            print('请支付{:.2f}元'.format(subtotal))
        elif membership == 'vip':
            subtotal = Vip(items, total).discount()
            print('请支付{:.2f}元'.format(subtotal))
        print('祝您生活愉快')


if __name__ == '__main__':
    Cash_register.checkout('vip', 2, 31)
