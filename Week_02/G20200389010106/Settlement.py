"""
为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：

普通用户消费不足 200 元，无折扣，原价付费；
普通用户消费满 200 元打九折；
VIP 会员满 200 元打八折；
VIP 会员满 10 件商品打八五折。
要求：
请使用面向对象编程实现结算功能。
由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。
"""

from abc import ABCMeta, abstractmethod
class Customer(object, metaclass=ABCMeta):
    """用户"""
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def pay_up(self):
        """
        结账
        :return: 价格
        """
        pass


class Ordinary(Customer):
    #普通用户
    def pay_up(self, price):
        if price < 0:
            return 0
        elif price < 200:
            return price
        elif price >=200:
            return price*0.9
            
class VIP(Customer):
    #VIP用户
    def pay_up(self, price, number):
        if price < 0 or number < 0:
            return 0
        if price < 200 and number < 10 :
            return price
        elif price < 200 and number >=10:
            return price * 0.85
        else :
            return price * 0.8

def main():
    customers = [ Ordinary('Sherry'), VIP('AAA') ]
    for custom in customers:
        if isinstance(custom, Ordinary):
            price = float(input('请输入普通会员%s的购买金额 ' % custom.name))
            print('亲爱的顾客%s需要支付: ￥%s元' %(custom.name, custom.pay_up(price)))
        elif isinstance(custom, VIP):
            price = float(input('请输入VIP会员%s的购买金额 ' % custom.name))
            number = float(input('请输入VIP会员%s的购买件数 ' % custom.name))
            print('尊敬的VIP会员%s需要支付: ￥%s元' %(custom.name, custom.pay_up(price, number)))

if __name__ == '__main__':
    main()