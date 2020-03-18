# coding:utf-8
# 为“996 便利店”设计一套销售系统的结算模块;
# 结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账

        
class Cashier():
    
    '''
    电商结算模块：
    1、普通用户消费不足200元，无折扣，原价付费；
    2、普通用户消费满200元打九折；
    3、VIP会员满200元打八折；
    4、VIP会员满10件商品打八五折。
    由于VIP会员存在两种折扣方式，需自动根据最优惠的价格进行结算
    '''

    def __init__(self, total_price, goods_account, is_vip):
        self.total_price = total_price
        self.goods_account = goods_account
        self.is_vip = is_vip
    
    
    def __normal_checkout(self):
        if self.total_price >= 200:
            return self.total_price * 0.9
        return self.total_price
       
          
    def __vip_checkout(self):
        if self.total_price >= 200:
            return self.total_price * 0.8
        elif self.goods_account >= 10:
            return self.total_price * 0.85
        else:
            return self.total_price
    
    
    def checkout(self):
        if self.is_vip:
            return self.__vip_checkout()
        return self.__normal_checkout()


# 普通用户消费不足200元，无折扣，原价付费        
c1 = Cashier(100, 1, False)
print(c1.checkout())

# 普通用户消费满200元打九折       
c2 = Cashier(200, 10, False)
print(c2.checkout())

# VIP会员无折扣，原价付费        
c3 = Cashier(100, 9, True)
print(c3.checkout())

# VIP会员满200元打八折       
c4 = Cashier(200, 1, True)
print(c4.checkout())

# VIP会员满10件商品打八五折 
c5 = Cashier(100, 10, True)
print(c5.checkout())

# VIP会员满200元,满10件商品,打八折 
c6 = Cashier(200, 10, True)
print(c6.checkout())
