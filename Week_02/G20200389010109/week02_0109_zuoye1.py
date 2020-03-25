# 为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户
# （普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：
# 普通用户消费不足 200 元，无折扣，原价付费；
# 普通用户消费满 200 元打九折；
# VIP 会员满 200 元打八折；
# VIP 会员满 10 件商品打八五折。
# 要求：
# 请使用面向对象编程实现结算功能。
# 由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。

class Shop_996(object):
    
    def __init__(self,name,goods):
        self.name = name
        goods = []
        self.goods = goods
        
    
class noVIP(Shop_996):
    def __init__(self,goods):
        super().__init__(goods)
    def novip_pay():
        price = 0
        for good in noVIP.goods:
            price += dict_goods[good]
        if price >= 200:
            price = price*0.9
        else:
            print('无折扣')
        return print('总计：%2f 元', float(price))

class VIP(Shop_996):
    def __init__(self,goods):
        super().__init__(goods)
    def vip_pay():
        price = 0
        nums = 0
        for good in VIP.goods:
            price += dict_goods[good]
            nums += 1
        if price >= 200 & nums>= 10:
            price = price*0.8
        elif price >=200:
            price = price*0.8
        elif nums>= 10:
            price = price*0.85
        else:
            print('无折扣')
        return print('总计：',float(price))
class Factory:
    def run(name,consumer):
        if consumer == 'vip':
            return VIP.vip_pay()
        else:
            return noVIP.novip_pay()

if __name__ == '__main__':
    dict_goods = {'apple':10,'pen':100,'car':200}   
    Shop_996.goods=['car']
    Factory.run(name='one',consumer='vip')