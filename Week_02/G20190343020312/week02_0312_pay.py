class Accounting(object):
    total_pay = 0  # 商品总价格
    total_goods = 0  # 商品总数

    def __init__(self, name, user_type, goods=None):
        self.name = name
        self.user_type = user_type  # 用户类型（0 ：普通用户  1：vip）
        if goods is None:
            goods = []
        self.goods = goods

    # 属性返回是否vip
    def is_vip(self):
        if (self.user_type == 0):
            return False
        else:
            return True

    def discount(func):
        def inner(self, *args):
            ret = func(self, *args)
            ret[0] = float(ret[0])
            if not self.is_vip():
                if ret[0] >= 200:
                    discount_pay = ret[0] * 0.9
                else:
                    discount_pay = ret[0]
            else:
                if ret[0] >= 200:
                    discount_pay = ret[0] * 0.8
                if ret[0] < 200 & ret[1] >= 10:
                    discount_pay = ret[0] * 0.85
            print(f'顾客{self.name}，你好：你需要支付{discount_pay: .2f}元') 
            # return discount_pay
        return inner
        


    def buy(self, *args):
        self.goods.append(*args)
    
    @property
    @discount
    def pay(self):
        for i in self.goods:
            for j in i:
                self.total_pay += j[1] * j[2]
                self.total_goods += j[2]
        self.total_pay = "{:.2f}".format(self.total_pay)
        l = [self.total_pay, self.total_goods]
        return l



        

# 执行入口
# 商品参数  商品名、单价、数量
if __name__ == '__main__':
    a = Accounting('小明', 1)
    a.buy([['Apple', 5.3, 60], ['Pear', 4.2, 4]])
    a.pay
