
from decimal import *


# 设置全局精度
getcontext().prec = 6

class product_info(object):
    product_name = ''
    product_price = 0
    # def __init__(self,good_name,good_price):
    #     self.good_name
    #     self.good_price
        

class payProduct(object):
    money = 0.00
    is_vip  = False
    product_list = []

    def __init__(self, is_vip, product_list):
        self.is_vip = is_vip
        self.product_list = product_list
        self._cost = 0
        
    @property
    def cost(self):
        return self._cost
    
    @cost.getter
    def cost(self):
        if self.product_list == None:
            print('good_list is none')
            return Decimal(0).quantize(Decimal('0.00'))
        #算出商品总费用
        product_sum_price = self.sum_product_price()
        if self.is_vip:
            #计算商品没打扰时，总费用
            product_sum_price2 = product_sum_price
            #判断总费用大于200时的花费
            if product_sum_price >= 200:
                product_sum_price = product_sum_price * 0.8
            ##计算商品数量大于10个时的花费
            if len(self.product_list) > 10:
                product_sum_price2 * 0.85
            #使用三目表达式，算出最优惠的费用
            return Decimal(product_sum_price if(product_sum_price2 > product_sum_price) else product_sum_price2).quantize(Decimal('0.00'))
        else:
            #如果是普通用户的，费用计算方式
            if product_sum_price >= 200:
                return Decimal(product_sum_price * 0.9).quantize(Decimal('0.00'))
            return Decimal(product_sum_price).quantize(Decimal('0.00'))
    
    def sum_product_price(self):
        if self.product_list == None:
            return 0
        sum = 0
        for i in range(len(self.product_list)):
            sum = sum + self.product_list[i].product_price
        print(sum)
        return sum


product_list = []
for i in range(0,20):
    # good = good_info(f'商品 {i}', i)
    product = product_info()
    product.product_name = f'商品 {i}'
    product.product_price = i*10
    product_list.append(product)
p = payProduct(True, product_list)
print(p.cost)
