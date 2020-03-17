# coding:utf-8
# 为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账


class Cashier(object):
    '''
    电商结算模块：
    1、普通用户消费不足200元，无折扣，原价付费；
    2、普通用户消费满200元打九折；
    3、VIP会员满200元打八折；
    4、VIP会员满10件商品打八五折。
    由于VIP会员存在两种折扣方式，需自动根据最优惠的价格进行结算
    '''

    '''
    customer = [(name: 'Jack', vip: True), ...]
    order = [(item: 'apple', price: 10), ...]
    '''
    def __init__(self, customer, order):
        self.customer = customer
        self.order = order


    def original_price(self):
        self.original_price = 0
        for item in self.order:
            original_price += item.price
        returm self.original_price

    
    def 


    def due(self):
        self.due = self.original_price * get_discount(customer, order)
        return self.due


    def __repr__(self):
    self.total()
    rep =  '欢迎光临996便利店'
    rep += '***************\n'
    rep += '客户名称: {}\n'.format(self.customer.name)
    rep += '===商品列表===\n'
    for item in self.order:
        rep += '商品名称: {}    价格: {}\n'.format(item.name, item.price)
    rep += '***************\n'
    rep += '原价：{} 元\n'.format(self.original_price)
    rep += '折后应付：{} 元'.format(self.due())
    return rep
    




