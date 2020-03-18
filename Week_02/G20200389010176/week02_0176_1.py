# coding:utf-8
# 为“996 便利店”设计一套销售系统的结算模块;
# 结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账

class Customer():
    def __init__(self, name, is_vip):
        self.name = name
        self.is_vip = is_vip
        

class Order():
    def __init__(self, customer, shopping_cart):
        self.customer = customer
        self.shopping_cart = shopping_cart
    
    @property
    def total_price(self):
        total_price = 0
        for item in self.shopping_cart:
            total_price += self.shopping_cart[item]
        return total_price
    
    @property
    def goods_account(self):
        return len(self.shopping_cart)
        
        
class Cashier():
    
    '''
    电商结算模块：
    1、普通用户消费不足200元，无折扣，原价付费；
    2、普通用户消费满200元打九折；
    3、VIP会员满200元打八折；
    4、VIP会员满10件商品打八五折。
    由于VIP会员存在两种折扣方式，需自动根据最优惠的价格进行结算
    '''
        
    def __init__(self, order):
        self.total_price = order.total_price
        self.goods_account = order.goods_account
        self.is_vip = order.customer.is_vip
    
    
    def __normal_checkout(self):
        if self.total_price >= 200:
            return self.total_price * 0.9
        return self.total_price
       
          
    def __vip_checkout(self):
        if self.total_price >= 200:
            return self.total_price * 0.8
        elif self.goods_account >= 10:
#            print('check')
            return self.total_price * 0.85
        else:
            return self.total_price
    
    
    def checkout(self):
        if self.is_vip:
            return self.__vip_checkout()
        return self.__normal_checkout()


c1 = Customer('Jack', False)
c2 = Customer('Lucy', True)

s_price100 = {'good1': 100}
s_price200 = {'good1': 200}
s_account10 = {f'good{i}':i for i in range(1,11)}
s_price200_account10 = {f'good{i}':i*5 for i in range(1,11)}


# 普通用户消费满200元打九折
o1 = Order(c1, s_price200)

# 普通用户消费不足200元，无折扣，原价付费 
o2 = Order(c1, s_price100)

# VIP会员满200元打八折 
o3 = Order(c2, s_price200)

# VIP会员满10件商品打八五折 
o4 = Order(c2, s_account10)

# VIP会员满200元,满10件商品,打八折 
o5 = Order(c2, s_price200_account10) 

# VIP会员无折扣，原价付费 
o6 = Order(c2, s_price100)

p1 = Cashier(o1)
print(f'原价：{p1.total_price} 折后应付：{p1.checkout()} 折扣：{10 * p1.checkout() / p1.total_price}')

p2 = Cashier(o2)
print(f'原价：{p2.total_price} 折后应付：{p2.checkout()} 折扣：{10 * p2.checkout() / p2.total_price}')

p3 = Cashier(o3)
print(f'原价：{p3.total_price} 折后应付：{p3.checkout()} 折扣：{10 * p3.checkout() / p3.total_price}')

p4 = Cashier(o4)
print(f'原价：{p4.total_price} 折后应付：{p4.checkout()} 折扣：{10 * p4.checkout() / p4.total_price}')

p5 = Cashier(o5)
print(f'原价：{p5.total_price} 折后应付：{p5.checkout()} 折扣：{10 * p5.checkout() / p5.total_price}')

p6 = Cashier(o6)
print(f'原价：{p6.total_price} 折后应付：{p6.checkout()} 折扣：{10 * p6.checkout() / p6.total_price}')
