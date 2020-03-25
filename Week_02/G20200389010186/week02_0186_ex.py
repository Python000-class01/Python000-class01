# 普通用户消费不足 200 元，无折扣，原价付费；
# 普通用户消费满 200 元打九折；
# VIP 会员满 200 元打八折；
# VIP 会员满 10 件商品打八五折。
# 由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。

class Custom(object):
    def __init__(self, price, count, level):
        self.price = price
        self.count = count
        self.level = level
    
    def getPrice(self):
        return self.price


class customUser(Custom):
    def __init__(self, price, count, level):
        super().__init__(price, count, level)

    def getPrice(self, price, count):
        if price < 200:
            return price
        elif price >= 200:
            return price * 0.9


class customVip(Custom):
    def __init__(self, price, count, level):
        super().__init__(price, count, level)

    def getPrice(self, price, count):
        if (price < 200) & (count < 10):
            return price
        elif(price < 200) & (count >= 10):
            return price * 0.85
        else:
            return price * 0.80


class Factory:
    def TotalPrice(self, price, count, level):
        if level == 'user':
            return customUser.getPrice(self, price, count)
        elif level == 'vip':
            return customVip.getPrice(self, price, count)


if __name__ == '__main__':
    factory = Factory()
    customuser_price = factory.TotalPrice(200, 10, 'user')
    customvip_price = factory.TotalPrice(200, 8, 'vip')

    print(customuser_price)
    print(customvip_price)