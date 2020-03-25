from good import Good

class MyGood(Good):
    #货物名、数量、价格
    def __init__(self, name, count, price):
        self.name = name
        self.count = count
        self.price = price

#商店
class Store(object):
    #默认账户金额
    account = 10000
    #接收的顾客列表
    customers = []
    #货物字典
    goods = []
    #初始化商店
    def __init__(self, account):
        self.account = account
    #接收顾客
    def accept(self, customer):
        customer.append(customer)
    #接收顾客的钱
    def receive(self, money):
        self.account = self.account + money
    #进货
    def stock(self, good):
        for myGood in self.goods:
            if myGood.name == good.name:
                myGood.price = good.price
                myGood.count = myGood.count + good.count
                return 
        self.goods.append(good)
    #判断是否含有某个商品
    def hasTheGood(self, good):
        for myGood in self.goods:
            if myGood.name == good.name:
                return True
        return False
    #根据名称取出商品
    def takeGoods(self, goodName):
        for myGood in self.goods:
            if myGood.name == goodName:
                return myGood
        return None
