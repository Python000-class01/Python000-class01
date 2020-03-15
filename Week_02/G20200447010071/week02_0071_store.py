from decimal import Decimal

goods = [
    {
        'name': 'Python进阶训练营',
        'price': 49
    },
    {
        'name': '前端训练营',
        'price': 59
    },
    {
        'name': '算法小课',
        'price': 9.9
    },
]


class Good(object):
    """ 商品类 """
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User(object):
    """ 用户类 """
    def __init__(self, name, role):
        self.name = name
        self.role = role

class DiscountBase(object):
    """ 折扣类 """
    def __call__(self, price):
        pass

class NormalNUmberDiscount(DiscountBase):
    """ 普通用户满10件商品打九折 """
    def __init__(self):
        self.name = '普通用户满10件商品打九折'

    def __call__(self, price):
        print('使用折扣: %s' % self.name)
        return Decimal(str(price)) * Decimal('0.9')



class VipPriceDiscount(DiscountBase):
    """ VIP会员满200元打八折 """
    def __init__(self):
        self.name = 'VIP会员满200元打八折'

    def __call__(self, price):
        print('使用折扣: %s' % self.name)
        return Decimal(str(price)) * Decimal('0.8')

class VipNumberDiscount(DiscountBase):
    """ VIP会员满10件商品打八五折 """
    def __init__(self):
        self.name = 'VIP会员满10件商品打八五折'

    def __call__(self, price):
        print('使用折扣: %s' % self.name)
        return Decimal(str(price)) * Decimal('0.85')


def discountByRole(func):
    """ 根据不同用户身份选择不同的结算方法 """
    def wrap(instance, **kwargs):
        user = kwargs['user']
        total_number = kwargs['total_number']
        total_price = kwargs['total_price']
        if user.role == 'normal':
            if total_number >= 10:
                func(instance, price=instance.discounts['normal_number_discount'](total_price))
            else:
                func(instance, price=total_price)
        elif user.role == 'vip':
            if total_price >= 200:
                func(instance, price=instance.discounts['vip_price_discount'](total_price))
            elif total_number >= 10:
                func(instance, price=instance.discounts['vip_number_discount'](total_price))
            else:
                func(instance, price=total_price)
    return wrap


def analyze_goodsList(func):
    """ 处理商品列表 """
    def wrap(instance, **kwargs):
        goodsList = kwargs['goodsList']
        total_number = 0
        total_price = 0
        for good in goodsList:
            total_number += good['number']
            total_price += Decimal(str(good['good'].price)) * Decimal(str(good['number']))
        func(instance, user=kwargs['user'], goodsList=kwargs['goodsList'], total_number=total_number, total_price=total_price)
    return wrap

class Store(object):
    """ 超市类 """
    def __init__(self):
        self.goods = [Good(good['name'], good['price']) for good in goods]
        self.discounts = {
            'normal_number_discount': NormalNUmberDiscount(),
            'vip_number_discount': VipNumberDiscount(),
            'vip_price_discount': VipPriceDiscount()
        }

    @analyze_goodsList
    @discountByRole
    def checkout(self, **kwargs):
        price = kwargs['price']
        print(f'价格为: {price}元')


Store_996 = Store()
# 同时满足VIP会员满200元打八折和VIP会员满10件商品打八五折  触发  VIP会员满200元打八折
Store_996.checkout(user=User('user01', 'vip'), goodsList=[{'good': Store_996.goods[1], 'number': 10}])
# 触发VIP会员满10件商品打八五折
Store_996.checkout(user=User('user01', 'vip'), goodsList=[{'good': Store_996.goods[2], 'number': 10}])
# 触发普通用户满10件商品打九折
Store_996.checkout(user=User('user01', 'normal'), goodsList=[{'good': Store_996.goods[2], 'number': 10}])
# 什么都不触发
Store_996.checkout(user=User('user01', 'normal'), goodsList=[{'good': Store_996.goods[0], 'number': 9}])


