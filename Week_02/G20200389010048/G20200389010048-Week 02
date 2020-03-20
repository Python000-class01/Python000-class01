from decimal import *


# 设置全局精度
getcontext().prec = 6


class good_info(object):
    good_name = ''
    good_price = 0
    # def __init__(self,good_name,good_price):
    #     self.good_name
    #     self.good_price


class payGood(object):
    money = 0.00
    is_vip = False
    good_list = []

    def __init__(self, is_vip, good_list):
        self.is_vip = is_vip
        self.good_list = good_list
        self._cost = 0

    @property
    def cost(self):
        return self._cost

    @cost.getter
    def cost(self):
        if self.good_list == None:
            print('good_list is none')
            return Decimal(0).quantize(Decimal('0.00'))
        #算出商品总费用
        good_sum_price = self.sumGoodPrice()
        if self.is_vip:
            #计算商品没打扰时，总费用
            good_sum_price2 = good_sum_price
            #判断总费用大于200时的花费
            if good_sum_price >= 200:
                good_sum_price = good_sum_price * 0.8
            ##计算商品数量大于10个时的花费
            if len(self.good_list) > 10:
                good_sum_price2 * 0.85
            #使用三目表达式，算出最优惠的费用
            return Decimal(good_sum_price if(good_sum_price2 > good_sum_price) else good_sum_price2).quantize(Decimal('0.00'))
        else:
            #如果是普通用户的，费用计算方式
            if good_sum_price >= 200:
                return Decimal(good_sum_price * 0.9).quantize(Decimal('0.00'))
            return Decimal(good_sum_price).quantize(Decimal('0.00'))

    def sumGoodPrice(self):
        if self.good_list == None:
            return 0
        sum = 0
        for i in range(len(self.good_list)):
            sum = sum + self.good_list[i].good_price
        print(sum)
        return sum


good_list = []
for i in range(0, 20):
    # good = good_info(f'商品 {i}', i)
    good = good_info()
    good.good_name = f'商品 {i}'
    good.good_price = i*10
    good_list.append(good)
p = payGood(True, good_list)
print(p.cost)
