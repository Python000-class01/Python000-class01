'''
超市管理系统，会员信息和产品信息存放在数据库中(Mongo)
1， 管理系统实例化时会连接到数据库
2， 管理系统提供增加/删除/更新会员信息功能
3， 管理系统提供增加/删除/更新商品信息功能
4， 管理系统提供结账功能，传入订单，将自动计算出折扣后的总价
'''
import pymongo
import order
import discount
import functools

class SuperMarket:

    def __init__(self):
        """创建数据库连接"""
        myclient = pymongo.MongoClient("mongodb://admin:admin@192.168.99.100:27017/")
        mydb = myclient["supermarket"]
        self.db = mydb

        #实例化折扣计算器
        dm = discount.dm
        self.dm = dm


    def insert_goods():
        """没时间写了"""
        pass

    def insert_customer():
        """没时间写了"""
        pass

    @functools.lru_cache() 
    def query_goods_price(self, name):
        """根据商品名称查询价格"""
        myquery = {"name":name}
        myprojection = {"price":1,"_id":0}

        price = self.db["product"].find_one(myquery, myprojection)

        assert price is not None, f'the product {name} is not exist in db...'

        return price.get("price")


    @functools.lru_cache() 
    def query_is_vip(self, mobile):
        """根据电话号码查询该客户是否为VIP"""
        myquery = {"mobile":mobile}
        myprojection = {"level":1,"_id":0}

        isvip = self.db["customer"].find_one(myquery,myprojection)

        if isvip is not None and isvip.get("level").find("vip") >=0 :
            return True
        
        return False

    def calc_pay(self, order):
        products = order.cart
        pay = 0

        for product in products:
            price = self.query_goods_price(product.name)
            pay += int(product.qy) * price
        
        return pay

    def calc_quantity(self, order):
        products = order.cart
        qy = 0

        for product in products:
            qy += int(product.qy)

        return qy


    
    def pay(self, order):
        '''计算订单总价，根据各种折扣规则'''
        '''计算折扣前订单总价'''
        pay = self.calc_pay(order)
        qy = self.calc_quantity(order)
        isvip = self.query_is_vip(order.customer.mobile)

        discount = min(discount_func(isvip, pay, qy) for discount_func in self.dm.discounts)
        final_pay = discount * pay
        print(f'price is {pay:.2f}, discount is {discount:.2f}, so final price is {final_pay:.2f}元')

        return final_pay
        

if __name__ == '__main__':
    sm = SuperMarket()
    
    """准备订单"""
    """1st type: vip用户数量和价格均达到，此时应该是8折"""
    Onomah = order.Customer('Onomah', '13500000001')
    cart   = [order.Product('apple', '2'), order.Product('orange', '30'), order.Product('pineapple', '10')]
    order1 = order.Order(Onomah, cart)

    sm.pay(order1)