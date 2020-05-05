#父类：1、变量初始化；2、打印支付信息的方法
class Customer(object):
    def __init__(self, name,total_goods, total_money):
        self.name = name
        self.total_money = total_money
        self.total_goods = total_goods

    def print_tips(self,name,total_money):
        print(f"亲爱的顾客{self.name},您需要支付{self.total_money:.2f}元")

#子类普通会员：结算方式的方法
class Customer_Normal(Customer):
    def __init__(self, name,total_goods, total_money):
        super().__init__(self, name,total_goods, total_money)

    def payup(self):
        if self.total_money < 200:
            super().print_tips(self.name,self.total_money)
        else:
            self.total_money = self.total_money * 0.9
            super().print_tips(self.name,self.total_money)

#子类VIP会员：结算方式的方法
class Customer_VIP(Customer):
    def __init__(self, name, total_goods, total_money):
        self.name = name
        self.total_money = total_money
        self.total_goods = total_goods

    def payup(self):
        if self.total_money < 200 and self.total_goods < 10 :
            super().print_tips(self.name,self.total_money)
        elif self.total_money < 200.0 and self.total_goods >= 10.0 :
            self.total_money = self.total_money * 0.85
            super().print_tips(self.name,self.total_money)
        else:
            self.total_money = self.total_money * 0.8
            super().print_tips(self.name,self.total_money)

#根据不同的会员调用不同的类
class Factory:
    def getPerson(self, name, level,total_goods, total_money):
        if level == 'Normal':
            customer = Customer_Normal(name, total_goods, total_money)
            return customer.payup()
        elif level == 'VIP':
            customer = Customer_VIP(name,  total_goods, total_money)
            return customer.payup()
        else:
            print("请输入正确的会员等级！")

if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("Adam", "VIP",20,19)