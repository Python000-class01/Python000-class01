# -*- coding: utf-8 -*-



#####  =================   定义顾客类，属性为顾客VIP编号(默认None), 提供购买结算方法  ===================
class Coustom(object):
    '''
            消费者有VIP编号 —— 可选择属性
            购买的物品清单（需要列印物品清单，单价，总金额）—— 用字典维护购买物品清单 {'购买物品’：(单价【浮点数】，数量【整数】)}
            行为：为购买付款 —— 打印出顾客需要支付的总金额
            '''


    #### ====================== 实例化时，只要传VIP编号，购买商品非属性      ======================

    def __init__(self):
        self.VIP_No = None

    ###  ====================== 获得购物清单，这个清单由商品类维护，此处省略======================

    def goods_list(self, goods):
        return goods

    ### ====================== 获取VIP编号 ===================================================

    def get_VIP_No(self):
        if VIP_No is not None:
            return VIP_No

    ########  ============================ 结算功能 ===========================================

    def pay(self, goods={}):
        total_pay = 0
        for key in goods:
            pay = goods[key][0] * goods[key][1]
            total_pay += pay
        return total_pay

####   ============================ 定义VIP消费者的付款装饰器 =============================

def decorate_VIP(func):
    def total_pay(*args,**kwargs):
        bill,num_of_goods = func(*args,**kwargs)
        if bill >= 200:
            bill_ordinary = bill * 0.8
            return bill_ordinary
        elif bill < 200 and num_of_goods >= 10:
            return bill* 0.85
        else:
            return bill
    return total_pay

####   ============================ 创建VIP消费者类 =======================================

class VIP_Coustom(Coustom):
    def __init__(self, VIP_No = None):
        super().__init__
        print('Hi,my dear VIP customer')

    ####   ============================ 运用装饰器重写父类pay方法 ===========================
    @decorate_VIP
    def pay(self,goods={}):
        num_of_goods = 0  ###记录消费者购买的商品总数量
        for key in goods:
            num_of_goods += goods[key][1]
        totalpay =  Coustom.pay(self,goods)
        return totalpay,num_of_goods



####   ============================ 定义普通消费者的付款装饰器 ============================

def decorate_ordinary(func):
    def total_pay(*args,**kwargs):
        bill = func(*args,**kwargs)
        if bill >= 200:
            bill_ordinary = bill * 0.9
            return bill_ordinary
        else:
            return bill
    return total_pay

####   ============================ 创建普通消费者类 ============================

class Ordinary_Coustom(Coustom):
    def __init__(self):
        super().__init__
        print('Hi,coustom')

    ####   ============================ 运用装饰器重写父类pay方法 ===========================
    @decorate_ordinary
    def pay(self,goods):
        totalPay = Coustom.pay(self,goods) ## 当我把self 参数传给Coustom时，需要把goods传给父类
        return totalPay
        

####   ============================ 创建消费者分类工厂，维护VIP列表，判断是否为VIP客户 ============================

class Factory:
    VIP_list = [1,2,3,4,5]
    def getCoustomer(self, VIP_No = None ):
        if VIP_No is not None:
            return VIP_Coustom()
        else:
            return Ordinary_Coustom()


if __name__ == '__main__':
    factory = Factory()
    goods = {'apple':(3.15,5),'banana':(2.0,3),'orange':(5.5,5)}
    goods2 = {'apple': (3.15, 50), 'banana': (2.0, 3), 'orange': (5.5, 100)}
    goods3 = {'apple': (3.15, 1), 'banana': (2.0, 2), 'orange': (5.5, 5)}

    coustomer_1 = factory.getCoustomer(3)
    print(coustomer_1.pay(goods))
    print(coustomer_1.pay(goods2))
    print(coustomer_1.pay(goods3))

    coustomer_2 = factory.getCoustomer()
    print(coustomer_2.pay(goods))

    print(coustomer_2.pay(goods2))
    print(coustomer_2.pay(goods3))