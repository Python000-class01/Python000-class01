#-*- coding:utf-8 -*-
import pandas as pd

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []
        self.discount_rate = 1
        self.goods_num = 0
        self.total_price = 0

    #添加至购物车并计算数量/金额
    def _cart_cal(self, goods):
        self.cart.extend(goods)
        self.goods_num, self.total_price = len(self.cart), sum(x[1] for x in self.cart)
    
    #结账：输出帐单与折扣
    @property
    def pay(self):
        df = pd.DataFrame(self.cart, columns=['Item','Price'])
        df.index += 1
        print('=' * 50)
        print(f'Customer Name: {self.name}')
        print(df)
        print(f'Number: {self.goods_num} | Total Price(before discount): {self.total_price}')
        print(f'Discount: {self.discount_rate} | Total Price: {self.total_price * self.discount_rate}')
        print('=' * 50)

    #清理购物车
    @property
    def clean(self):
        self.__init__(self.name)

#VIP顾客
class Vip_Customer(Customer):
    def __init__(self,name):
        self.name = name
        super().__init__(name)
    
    def add_to_cart(self, goods):
        super()._cart_cal(goods)
        if self.total_price >= 200:
            self.discount_rate = 0.8
        elif self.goods_num >= 10:
            self.discount_rate = 0.85
    
#普通顾客
class Normal_Customer(Customer):
    def __init__(self,name):
        self.name = name
        super().__init__(name)

    def add_to_cart(self, goods):
        super()._cart_cal(goods)
        if self.total_price >= 200:
            self.discount_rate = 0.9


if __name__=="__main__":
    customer_1 = Vip_Customer(name='customer_1')
    customer_2 = Normal_Customer(name='customer_2')
    #VIP顾客不折扣
    customer_1.add_to_cart([[f'Product-{i}',10] for i in range(1,6)])
    customer_1.pay
    customer_1.clean
    #VIP顾客85折
    customer_1.add_to_cart([[f'Product-{i}',10] for i in range(1,11)])
    customer_1.pay
    customer_1.clean
    #VIP顾客8折
    customer_1.add_to_cart([[f'Product-{i}',50] for i in range(1,6)])
    customer_1.pay
    customer_1.clean
    #普通顾客无折扣
    customer_2.add_to_cart([[f'Product-{i}',10] for i in range(1,6)])
    customer_2.pay
    customer_2.clean
    #普通顾客9折
    customer_2.add_to_cart([[f'Product-{i}',50] for i in range(1,6)])
    customer_2.pay
    customer_2.clean


