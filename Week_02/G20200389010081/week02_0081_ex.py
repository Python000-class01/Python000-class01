'''
为“996 便利店”设计一套销售系统的结算模块，
结算模块要求对不同类型的用户（普通用户、VIP 用户）的
单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：

普通用户消费不足 200 元，无折扣，原价付费；
普通用户消费满 200 元打九折；
VIP 会员满 200 元打八折；
VIP 会员满 10 件商品打八五折。
要求：

请使用面向对象编程实现结算功能。
由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。

'''


class Iidentity(object):
    def __init__(self, user_identity=0):  # user_identity默认普通用户  0:普通用户；1:VIP
        self.user_identity = user_identity
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(instance, self.user_identity)

    def __set__(self, instance, value):
        value = int(value)
        if value not in range(2):
            raise ValueError('must be in (0-1)')
        if value == 1:
            self.data[instance] = 'VIP用户'
        else:
            self.data[instance] = 'Common用户'


class PaySystem(object):
    user_identity = Iidentity()
    def __init__(self):
        self.list_total = []

    # 录入商品价格
    def record(self, vlaue):
        self.list_total.append(int(vlaue))
        return self.list_total

    # 按照对应身份结算
    def pay_balance(self):
        sum_pay = 0
        if self.user_identity == 'Common用户':
            '''
            普通用户消费不足 200 元，无折扣，原价付费；
            普通用户消费满 200 元打九折；
            '''
            for i in self.list_total:
                sum_pay += i
            if sum_pay > 200:
                sum_pay *= 0.9
            return sum_pay

        if self.user_identity == 'VIP用户':
            '''
            VIP 会员满 200 元打八折；
            VIP 会员满 10 件商品打八五折。
            '''
            for i in self.list_total:
                sum_pay += i
            if sum_pay < 200 and len(self.list_total) > 10:
                sum_pay *= 0.85
            elif sum_pay > 200:
                sum_pay *= 0.8
            return sum_pay


if __name__ == '__main__':
    user = PaySystem()
    user.user_identity = input("请输入用户身份ID：0/普通用户，1/VIP用户:")
    price = None
    num = 0
    while True:
        num += 1
        price = input("{}:".format(num))
        if price == '#':
            break
        user.record(price)
    print('本次{}消费一共：{}'.format(user.user_identity, user.pay_balance()))
