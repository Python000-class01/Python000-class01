# 实现“996 便利店”销售系统的结算模块
# 用户类
class User(object):
    def __init__(self, name):
        self._name = name
        self._memberrank = ''
        self._shoppingcart = {}
        self._productamount = 0

    def add_to_shoppingcart(self, productno, productnum=1):
        if self._shoppingcart.keys().__contains__(productno) == False:
            self._shoppingcart[productno] = 0
        self._shoppingcart[productno] += productnum
        self._productamount += productnum

    def remove_From_shoppingcart(self, productno, productnum=1):
        if self._shoppingcart.keys().__contains__(productno) == False:
            return
        if self._shoppingcart[productno] < 0:
            return
        productnum0 = productnum
        if self._shoppingcart[productno] < productnum0:
            productnum0 = self._shoppingcart[productno]
        self._shoppingcart[productno] -= productnum0
        self._amount -= productnum0

    @property
    def name(self):
        return self._name

    @property
    def memberrank(self):
        return self._memberrank

    @property
    def shoppingcart(self):
        return self._shoppingcart

    @property
    def productamount(self):
        return self._productamount


# 普通用户类
class CommonUser(User):
    def __init__(self, name):
        super().__init__(name)
        self._memberrank = '普通会员'


# VIP用户类
class VIPUser(User):
    def __init__(self, name):
        super().__init__(name)
        self._memberrank = 'VIP会员'

# 结算方式
class CashMode(object):
    def __init__(self, user):
        self.user = user
        self._sumprice = 0

    def compute_price(self):
        for productno in self.user.shoppingcart:
            self._sumprice += Shop996.productPrices[productno] * self.user.shoppingcart[productno]
            print(f'商品{productno}：单价：{Shop996.productPrices[productno]}，'
                  f'{self.user.shoppingcart[productno]}件，小计：{self._sumprice}元')
        print(f'用户{self.user.name}本次购买商品总计：{self._sumprice}元')

        return self._sumprice

# 普通用户结算方式
class CommonCashMode(CashMode):
    # def __init__(self, user):
    #     super().__init__(user)

    def compute_price(self):
        super().compute_price()
        if self._sumprice >= 200:
            self._sumprice *= 0.9
            print('【普通会员】满200元享有9折优惠')
        return self._sumprice

# VIP用户结算方式
class VIPCashMode(CashMode):
    # def __init__(self, user):
    #     super().__init__(user)

    def compute_price(self):
        super().compute_price()
        # sumprice1 = self._sumprice
        # sumprice2 = self._sumprice
        if self._sumprice >= 200:
            self._sumprice *= 0.8
            print('【VIP会员】满200元享有8折优惠')
        elif self.user.productamount >= 10:
            self._sumprice *= 0.85
            print('【VIP会员】满10件商品享有8.5折优惠')
        return self._sumprice

# 工厂类，用于创建结算方式对象与用户对象
class Factory(object):
    def getCashMode(self, user):
        if type(user) is CommonUser:
            return CommonCashMode(user)
        else:
            return VIPCashMode(user)

    def getUser(self, name, tp='C'):
        if tp == 'C':
            return CommonUser(name)
        else:
            return VIPUser(name)

# 结算模块，用于对用户的一次购物进行计算
class PaymentModule(object):
    # 计算并输出当前用户需支付的金额
    def print_payinfo(self, user):
        _user = user
        _cashmode = Factory().getCashMode(user)
        print(f'用户【{_user.name}】为【{_user.memberrank}】，本次消费需支付：{_cashmode.compute_price()}元')

# 简单模拟996商店，目前只有商品与一个结算模块
class Shop996(object):
    # productInfos = {'001':'脉动'}
    productPrices = {'001': 4, '002': 10, '003': 15, '004': 19, '005': 13,
                     '006': 78, '007': 100, '008': 80, '009': 60, '010': 50,
                     '011': 300, '012': 111, '013': 31, '014': 41, '015': 51}
    paymentmodule = PaymentModule()

# 程序入口
if __name__ == '__main__':
    fact = Factory()
    user1 = fact.getUser('张珊')
    user1.add_to_shoppingcart('001',2)
    user1.add_to_shoppingcart('004',4)
    user1.add_to_shoppingcart('005',3)
    user1.add_to_shoppingcart('007',1)
    user1.add_to_shoppingcart('009',2)
    Shop996.paymentmodule.print_payinfo(user1)

    user2 = fact.getUser('李小勇')
    user2.add_to_shoppingcart('007',1)
    user2.add_to_shoppingcart('002',1)
    Shop996.paymentmodule.print_payinfo(user2)

    user3 = fact.getUser('王伟', 'V')
    user3.add_to_shoppingcart('001', 2)
    user3.add_to_shoppingcart('004', 4)
    user3.add_to_shoppingcart('005', 3)
    user3.add_to_shoppingcart('007', 1)
    user3.add_to_shoppingcart('009', 2)
    Shop996.paymentmodule.print_payinfo(user3)

    user4 = fact.getUser('马大脚', 'V')
    user4.add_to_shoppingcart('001', 10)
    user4.add_to_shoppingcart('002', 1)
    Shop996.paymentmodule.print_payinfo(user4)

    user5 = fact.getUser('马小帅', 'V')
    user5.add_to_shoppingcart('001', 1)
    Shop996.paymentmodule.print_payinfo(user5)
