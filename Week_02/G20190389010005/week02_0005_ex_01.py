"""
为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）
的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：

    1、普通用户消费不足 200 元，无折扣，原价付费；
    2、普通用户消费满 200 元打九折；
    3、VIP 会员满 200 元打八折；
    4、VIP 会员满 10 件商品打八五折。
要求：
    请使用面向对象编程实现结算功能。由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。

思路：
    1、定义一个顾客类
      属性：
        用户ID
        用户名称
        是否是 VIP （单纯从解决此题出发，如果 VIP 有更多可以使用继承区分不同用户）

      方法：
        购买商品，添加商品到购物车
        清空购物车

    2、定义商品类
      属性：
        商品ID
        商品名称
        商品单价
        库存

    3、购物车 -- 实际生产中应该有购物车以及购物车明细，此处就是购物车明细
       属性：
        用户ID
        商品ID
        商品数量
        商品单价



    4、定义一个便利店类
      属性：
        名称
        商品集合

      方法：
        进货
        结算

"""
from functools import reduce
import random


# 顾客类，实际生成中将属性定义成私有属性，使用@property取值或者@属性.setter 设置值
class Customer(object):

    def __init__(self, cid, name, isvip):
        self.cid = cid
        self.name = name
        self.is_vip = isvip
        self.cart_items = []

    def buy(self, goods, amount):
        cart_item = CartItem(self.cid, goods, amount)
        self.cart_items.append(cart_item)

    def clear_cart_items(self):
        self.cart_items.clear()


# 商品类
class Goods(object):

    def __init__(self, gid, name, price, stock):
        self.gid = gid
        self.name = name
        self.price = price
        self.stock = stock


# 购物车
class CartItem(object):

    def __init__(self, cid, goods, amount):
        self.cid = cid
        self.goods = goods
        self.amount = amount


# 便利店类
class ConvenienceStore(object):

    def __init__(self, name):
        self.name = name
        self.goods = []

    # 进货
    def purchase(self, goods):
        self.goods.append(goods)



    # 结算
    # 1、普通用户消费不足200元，无折扣，原价付费；
    # 2、普通用户消费满 200元打九折；
    # 3、VIP会员满200元打八折；
    # 4、VIP会员满10件商品打八五折，由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。
    @staticmethod
    def settle_accounts(self, customer):
        if customer is None:
            print("Customer cannot be none.")
            return
        cart_items = customer.cart_items
        if not len(cart_items):
            print("Please select product to settle.")
            return

        # 校验商品库存是否足够
        # TODO

        # 计算总金额
        total_amount = reduce(lambda x, y: x + y, map(lambda g: g.goods.price, cart_items))
        print('商品总金额{}'.format(total_amount))

        is_vip = customer.is_vip
        # 普通会员
        if not is_vip:
            # 满200打9折
            if total_amount >= 200:
                total_amount = total_amount * 0.9

            total_amount = round(total_amount, 2)
            print('用户{0}最终需要支付的价格为：{1}'.format(customer.name, total_amount))
            # 扣库存
            # TODO
            # 清空购物车
            customer.clear_cart_items()

            return total_amount
        else:
            # VIP 会员
            amounts = reduce(lambda x, y : x + y, map(lambda c:c.amount, cart_items))

            print('用户购买商品数量：{}'.format(amounts))
            if total_amount < 200 and amounts < 10:
                pass

            if total_amount > 200 and amounts < 10:
                total_amount = total_amount * 0.8, 2

            if total_amount < 200 and amounts > 10:
                vip_amount = total_amount * 0.85
                print('用户超过10件后打折后的金额：{}'.format(vip_amount))
                total_amount = vip_amount if total_amount > vip_amount else total_amount

            if total_amount > 200 and amounts > 10:
                vip_amount = total_amount * 0.85
                discount_price = total_amount * 0.8
                total_amount = vip_amount if discount_price > vip_amount else discount_price

            total_amount = round(total_amount, 2)
            print('用户{0}最终需要支付的价格为：{1}'.format(customer.name, total_amount))

            # 扣掉库存
            # TODO

            # 清空购物车
            customer.clear_cart_items()

            return total_amount


def main():

    # 初始化账户
    customer = Customer(1, 'Tony', True)

    # 初始化商品
    purchase_goods = []

    for i in range(1, 100):
        price = round(random.random() * 10, 2)
        stock = round(random.random() * 100)
        goods = Goods(i, "商品%s" % str(i), price, stock)

        purchase_goods.append(goods)
        if i < 20:
            # 用户购买，添加到购物车
            customer.buy(goods, i)

    # 996便利店进货
    store = ConvenienceStore("996")
    store.purchase(purchase_goods)

    # 结算
    ConvenienceStore.settle_accounts(store, customer)


if __name__ == '__main__':
    main()
