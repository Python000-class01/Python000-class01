# 作业一：
# 为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：
# ----------普通用户消费不足 200 元，无折扣，原价付费；
# ----------普通用户消费满 200 元打九折；
# ----------VIP 会员满 200 元打八折；
# ----------VIP 会员满 10 件商品打八五折。
# 要求：
# ----------请使用面向对象编程实现结算功能。
# ----------由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。
# 作业二：
# 复习函数装饰器、类装饰、装饰器带参数与魔术方法的功能，参考官方文档熟悉魔术方法对应的 Python 内置方法。

# 参考网站： https://docs.python.org/zh-cn/3.7/reference/datamodel.html


'''
思路：
1、普通用户和 VIP 所购买产品信息计算方法完全一致：计算购买商品数量，计算购买商品价格一致
2、普通用户和VIP结算方式不同：定制不同的结算方法

customer父类：normal_customer 子类 + vip_customer 子类
1、在customer父类中定义购买产品信息计算方法
2、在customer父类中定义付款方法（适用于普通用户）
3、在vip_customer子类中重新定义付款方法（适用于VIP用户）覆盖父类的付款方法

实例化后每次购买产品输入：商品名称 + 价格
'''

class customer(object):
    def __init__(self, name, goods=None):
        if goods is None:
            goods = []
        self.name = name
        self.goods = goods
        self.price = 0.0  #初始化价格

    # 普通用户和VIP共同具有的属性：购买行为。包括购买商品，计算商品个数，及总价格
    def buy(self, goods_name, goods_price):
        self.goods.append(goods_name)
        # Globle goods_num = len(self.goods)
        self.price += goods_price
        self.goods_num = len(self.goods)

    def pay(self):
        print(f'the number of gooods is: {self.goods_num}')
        print(f'the total price is: {self.price}')

        if self.price < 200:
            print(f'you need pay: {self.price}') 
        else:
            print('you need pay:', round(self.price * 0.9, 1))

        #付款结束后，购物篮和总价清零
        self.price = 0.0
        self.goods = []


# 普通用户按父类默认属性方法付账
class normal_customer(customer):
        pass


# VIP 用户除重写付费规则外，继承父类所有属性方法
class vip_customer(customer):
    def pay(self):
        print(f'the number of gooods is: {self.goods_num}')
        print(f'the total price is: {self.price}')

        #付款判断条件
        if self.price < 200 and (self.goods_num < 10):
            print(f'you need pay: {self.price}')
        elif self.price < 200 and self.goods_num >= 10:
            print(f'you need pay: {round(self.price * 0.85, 1)}')
        else:
            print(f'you need pay:{round(self.price * 0.8, 1)}')

        #付款结束后，购物篮和总价清零
        self.price = 0.0
        self.goods = []


customer1 = normal_customer('heryhenry')
customer1.buy('goods1',10.5)
customer1.buy('goods2',12)
customer1.buy('goods3',13)
customer1.buy('goods4',14)
customer1.buy('goods5',15)
customer1.buy('goods6',16)
customer1.buy('goods7',17)
customer1.buy('goods8',18)
customer1.buy('goods9',19)
customer1.buy('goods10',20)
customer1.buy('goods11',200)

customer1.pay()

customer2 = vip_customer('seabrezer')
customer2.buy('goods1',11)
customer2.buy('goods2',12)
customer2.buy('goods3',13)
customer2.buy('goods4',14)
customer2.buy('goods5',15)
customer2.buy('goods6',16)
customer2.buy('goods7',17)
customer2.buy('goods8',18)
customer2.buy('goods9',19)
customer2.buy('goods10',20)
customer2.buy('goods11',200)

customer2.pay()
