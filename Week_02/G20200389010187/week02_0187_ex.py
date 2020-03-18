# user类-不知道pyhont是否支持接口
class User(object):
    # 初始化用户
    def __init__(self, monetory, quantity):
        # 消费金额
        self.monetory = monetory
        # 支付金额
        self.amount = []
        # 购买数量
        self.quantity = quantity

    # 支付
    def pay(self):
        pass


# 普通用户
class CommonUser(User,monetory, quantity):
    # 构造函数
    def __init__(self, monetory, quantity):
        super().__init__(self, monetory, quantity)

    # 普通用户支付
    def pay(self):
        if self.monetory < 200:
            self.amount = self.monetory
        else:
            self.amount = self.monetory * 0.9
        return self.amount

# vip用户
class VipUser(User):
    # 构造函数
    def __init__(self, monetory, quantity):
        super().__init__(self, monetory, quantity)

    # VIP用户支付
    def pay(self, instance, owner):
        if self.quantity >= 10:
        self.amount = self.monetory * 0.85
        if self.monetory < 200:
            self.amount = self.monetory
        else:
            self.amount = self.monetory * 0.8
        return self.amount

if __name__ == '__main__':
     user_id = input("结算时请确认用户类型：普通用户输入0，VIP用户输入1:")
     quantity = input("输入结算数量:")
     monetory = input("输入消费金额:")

     if user_id == 0:
         user CommonUser(monetory,quantity)
     if user_id == 1:
         user VipUser(monetory,quantity)

     user.pay();