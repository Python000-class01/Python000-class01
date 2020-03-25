# 996便利店结算模块
class Customer(object):
    def __init__(self, name, grand, goods):
        self.name = name
        self.grand = grand
        self.goods = goods

    def pay(self):
        if(self.grand == 'com'):
            sum1 = 0
            for items in self.goods:
                sum1 += int(items[1])
            if(sum1 >= 200):
                sum = sum1 * 0.9
            else:
                sum = sum1
            print('%s 消费了 %s 元' % (self.name, str(sum)))
        elif(self.grand == 'vip'):
            sum2 = 0
            sum3 = 0
            for items in self.goods:
                sum2 += int(items[1])
            for items in self.goods:
                sum3 += int(items[1])
            if(sum2 > 200):
                sum2 = sum2 * 0.8
                # print(sum2)
            if(len(self.goods) >= 10):
                sum3 = sum3 * 0.85
                # print(sum3)

            sum = min(sum2, sum3)
            print('%s 消费了 %s 元' % (self.name, str(sum)))


# 普通用户，消费不足200元
goods1 = [['apple', 10], ['Bear', 20]]
custom1 = Customer('Tom', 'com', goods1)
custom1.pay()
# 普通用户，消费超过200元
goods2 = [['apple', 10], ['Wine', 200]]
custom2 = Customer('Jerry', 'com', goods2)
custom2.pay()
# VIP用户，消费超过200元
goods3 = [['apple', 10], ['Wine', 200]]
custom3 = Customer('Mars', 'vip', goods3)
custom3.pay()
# VIP用户，消费超过200元，商品数量超过10
goods4 = [['apple', 10], ['Wine', 200], ['Bear', 200], ['Beef', 50], ['Milk', 10]
          , ['Chicken', 30], ['Goose', 100], ['Fish', 50], ['Water', 10], ['Suger', 5]
          , ['Icecream', 20]]
custom4 = Customer('Doris', 'vip', goods4)
custom4.pay()