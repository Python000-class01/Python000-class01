# 父类
class Customer(object):
    def __init__(self,purchased_num):
        self.purchased_num = purchased_num

    def walk(self):
        print('I can walk')

# 子类
class Normal(Customer):
    def __init__(self,price):
        self.price = price
    def cal(self):
        if (self.price >= 200):
            print(self.price*0.9)
            return self.price*0.9
        else:
            print(self.price)
            return self.price

class VIP(Customer):
    def __init__(self,purchased_num,price):
        self.purchased_num = purchased_num
        self.price = price
    def cal(self):
        price_a = 0
        price_b = 0
        if (self.price >= 200 and self.purchased_num >= 10):
            price_a = self.price*0.8
            price_b = self.price * 0.85
            print(min(price_a, price_b))
            return min(price_a, price_b)
        if(self.purchased_num >= 10):
            print(self.price*0.85)
            return self.price*0.85
        if (self.price >= 200):
            print(self.price * 0.8)
            return self.price*0.8

p1 = Normal(180)
p1.cal()
p2 = VIP(15,200)
p2.cal()