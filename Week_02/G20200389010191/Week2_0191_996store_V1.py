from collections import namedtuple

Order = namedtuple('Order', ['name', 'dots'])

Trr = namedtuple('Trr', ['name', 'price'])

class Cash(object):
    """实现结算"""
    def __init__(self, order, cater, using_promo=None):
        self.order = order
        self.cater = cater
        self.promo = using_promo

    def total(self):
        self.total_price = 0
        for item in self.cater:
            self.total_price += item.price
        return self.total_price
    def due(self):
        return self.total_price - self.promo(self.order, self.cater, self.total_price)

    def __repr__(self):
        self.total()
        rep = '===顾客信息===\n'
        rep += '购买人名称: {}\n'.format(self.order.name)
        rep += '===商品===\n'
        for item in self.cater:
            rep += '品名: {}    价格: {}\n'.format(item.name, item.price)
        rep += '===结算===\n'
        rep += '总价：{}\n'.format(self.total_price)
        rep += '优惠后价格：{}'.format(self.due())
        return rep

# 一个用来存储打折函数的列表
promos = []
def promo(promo_func):
    """打折函数装饰器"""
    promos.append(promo_func)
    return promo_func

@promo    # 它是一个折扣函数
def normal_promo(order, cater, total_price):
    """如果Normal用户消费高于200，就给予9折(1-0.9)"""
    if order.dots =='Normal':
        if total_price >= 200:
            return total_price * 0.1
        else:
            return 0

@promo    # 它是一个折扣函数
def vip_past_promo(order, cater, total_price):
    """如果Normal用户消费高于200，就给予8折"""
    if order.dots =='Vip':
        if total_price >= 200:
            return total_price * 0.2
        else:
            return 0

@promo    # 它是一个折扣函数
def up_ten_promo(order, cater, total_price):
    """VIP: 如果购物车内商品满或多于10个，则给予8.5折优惠"""
    if order.dots =='Vip':
        if len(cater) >= 10:
            return total_price * 0.15
        else:
            return 0

def best_promo(order, cater, total):
    """找到并推荐最佳折扣，按最佳折扣计算"""
    return max(found_promo(order, cater, total) for found_promo in promos)    # 试验每一个优惠，使用最好的结果


ben = Order('Ben', 'Vip')
ben_cash = Cash(order=ben, cater=[Trr('sock', 300), ], using_promo=vip_past_promo)
print(ben_cash, '\n')

ming = Order('XiaoMing', 'Vip')
ming_cash = Cash(order=ming, cater=[Trr('sth', 130), Trr('sth', 130), Trr('sth', 130),

                                    Trr('sth', 130), Trr('sth', 130), Trr('sth', 130),

                                    Trr('sth', 130), Trr('sth', 130), Trr('sth', 130), Trr('sth', 130)], using_promo=up_ten_promo)
print(ming_cash, '\n')
