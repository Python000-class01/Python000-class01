class Custom(object):
    # 顾客
    def __init__(self, goods=None):
        if goods is None:
            goods = []
        self.goods = goods
        self.price = 0
    
    def buy(self, goods_name):
        # 购买物品
        self.goods.append(goods_name)
        self.price += 5
    
    def pay_up(self,account):
        # 结账
        for item in self.goods:
            print(item)
        if len(self.goods) >= 10 and account == 'vip' and self.price < 200:
            self.price *= 0.85
        if self.price >= 200:
            if account == 'vip':
                self.price *= 0.8
            else:
                self.price *= 0.9
        print(self.price)

custom1 = Custom()
for i in range(20):
    custom1.buy('apple')
custom1.pay_up('vip')

custom2 = Custom()
for i in range(40):
    custom2.buy('apple')
custom2.pay_up('vip')

