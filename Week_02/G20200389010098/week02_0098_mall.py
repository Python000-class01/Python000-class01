import pandas as pd
import numpy as np
#模拟数据库存储用户商品信息
user = [{"uid": 1, "user_name": "customer_1", "is_vip": 0},
        {"uid": 2, "user_name": "customer_vip", "is_vip": 1}]
goods = [{"gid": 1, "goods_name": "coffee", "price": 25.25},
         {"gid": 2, "goods_name": "water", "price": 10.11},
         {"gid": 3, "goods_name": "bread", "price": 30.55},
         {"gid": 4, "goods_name": "desk", "price": 55.22}]
class MyMall:
    def __init__(self, uid):
        self.user_info = self.findUser(uid)
        # 用户不存在报错
        if(self.user_info == False):
            print("对不起，用户不存在")
        self._cart = []

    # 模拟查询用户
    def findUser(self, uid):
        rs = [x for x in user if (x['uid'] == uid)]
        if len(rs) > 0:
            return rs[0]
        else:
            return False

    # 属性返回是否vip
    @property
    def is_vip(self):
        if (self.user_info == False):
            return False
        else:
            if (self.user_info['is_vip'] == 0):
                return False
            else:
                return True

    # 模拟查询商品
    def findGoods(self, gid):
        rs = [x for x in goods if (x['gid'] == gid)]
        if len(rs) > 0:
            return rs[0]
        else:
            return False
    # 装饰器，处理优惠信息，pandas展示更直观
    def discount(func):
        def inner(self, *args, **kwargs):
            ret = func(self, *args, **kwargs)
            discount_fee = 0
            count = np.sum([x['num'] for x in ret])
            total = np.sum([x['num'] * self.findGoods(x['gid'])['price'] for x in ret])
            if not self.is_vip:
                if total >= 200:
                    discount_fee = np.around(total - np.around(total * 0.9, 2))
            else:
                if total >= 200:
                    discount_fee = np.around(total - np.around(total * 0.8, 2))
                if count >= 10:
                    temp = np.around(total - np.around(total * 0.85, 2))
                    if temp > discount_fee:
                        discount_fee = temp
            names = [self.findGoods(x['gid'])['goods_name'] for x in ret]
            info = [[self.findGoods(x['gid'])['price'], x['num'], np.around(x['num'] * self.findGoods(x['gid'])['price'], 2)] for x in
                    ret]
            names.append('-' * 10)
            info.append(['-' * 10, '-' * 10, '-' * 10])
            names.append("discount")
            info.append(['', '', -1*discount_fee])
            names.append("sum")
            info.append(['', count, total-1*discount_fee])
            df = pd.DataFrame(info, index=names, columns=['price', 'num', 'sum'])  # 生成6行4列位置
            return df
        return inner

    # 获取购物车，用装饰器生成优惠
    @property
    @discount
    def cart(self):
        return self._cart

    # set购物车的值，这里只做property的复习，实际不需要
    @cart.setter
    def addCart(self, info):
        gid = 0
        num = 1
        if(isinstance(info, int)):
            gid = info
        elif (isinstance(info, list)):
            gid = info[0]
            num = info[1]
        self._cart.append({"gid": gid, "num": num})

mall = MyMall(2)
mall.addCart = 1
mall.addCart = [2, 20]
print(mall.cart)
