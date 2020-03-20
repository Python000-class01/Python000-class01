
# 消费者
class Customer(object):
    def __init__(self,isVIP):
        self.isVIP = isVIP
        self.goods = []
        self.total_price = 0
        self.total_count = 0

    # 购买
    def buy(self, item, price, count):
        self.total_price += price * count
        self.total_count += count

    # 结账
    def bill(self):
        if self.isVIP:
            if self.total_price >= 200:
                return self.total_price * 0.8
            elif self.total_count >= 10:
                return self.total_price * 0.85
        else:
            if self.total_price >= 200:
                return self.total_price * 0.9
            else:
                return self.total_price


if __name__ == '__main__':

    # 消费者
    c = Customer(True)
    c.buy('itemA',100,2)
    c.buy('itemB',50, 2)
    print(c.bill())





