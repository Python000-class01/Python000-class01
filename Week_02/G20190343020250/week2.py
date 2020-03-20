class UserIdentity(object):
    # 定义用户身份，0为普通用户，1为VIP用户
    def __init__(self, user_id=0):
        self.user_id = user_id
        self.data = {}
    #使用数据描述器get、set
    def __get__(self,instance, owner):
        return self.data.get(instance, self.user_id)

    def __set__(self, instance, value):
        value = int(value)
        if value not in range(2):
            raise ValueError('输入值为0或1')
        if value == 1:
            self.data[instance] = 'VIP用户'
        else:
            self.data[instance] = '普通用户'


class PaymentSys(object):
    user_id = UserIdentity()
    def __init__(self):
        self.list_goods = []

    # 按商品价格统计
    def goods(self, price):
        self.list_goods.append(int(price))
        return self.list_goods

    # 结算时按照打折规则
    def goods_pay(self):
        sum_price = 0
        discount = '无折扣！'
        if self.user_id == '普通用户':
            for i in self.list_goods:
                sum_price += i
            if sum_price >= 200:
                sum_price *= 0.9
                discount = '享受九折优惠！'
            return sum_price,discount

        if self.user_id == 'VIP用户':
            for i in self.list_goods:
                sum_price += i
            #满10件商品可打八五折
            if sum_price < 200 and len(self.list_goods) > 10:
                sum_price *= 0.85
                discount = '享受八五折优惠！'
            elif sum_price >= 200:
                sum_price *= 0.8
                discount = '享受八折优惠！'
            return sum_price,discount


if __name__ == '__main__':
    user = PaymentSys()
    user.user_id = input("结算时请确认用户类型：普通用户输入0，VIP用户输入1:")
    pay = None
    num = 0
    while True: #输入c结束商品价格录入
        num += 1
        pay = input("（单位：元）商品{0:d}:".format(num))
        if pay == 'c':
            print('商品录入完毕！\n')
            break
        user.goods(pay)
    print('{}本次消费共：{}'.format(user.user_id, user.goods_pay()))