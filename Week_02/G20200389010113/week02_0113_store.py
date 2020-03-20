class Customer(object):
    def __init__(self, money, goods_count=None):
        self._discount = 1
        self.money = money
        self.goods_count = goods_count

    def check_out(self):
        print(f'{self}结账，折扣为{self.discount}，原价{self.money}，折扣价为{self.money*self.discount}')


class OrdinaryCustomer(Customer):
    def __init__(self, money):
        super().__init__(money)

    @property
    def discount(self):
        if self.money >= 200:
            self._discount = 0.9
        return self._discount

    def __repr__(self):
        return '普通客户'


class VIPCustomer(Customer):
    def __init__(self, money, goods_count=None):
        super().__init__(money, goods_count)

    @property
    def discount(self):
        # VIP 打折情况如下：
        # 总额超过200，但数量没有超过10，折扣为0.8
        # 总额超过200，数量超过10，根据各自计算结果取较小值
        # 总额没有超过200， 数量没有超过10， 不打折
        # 总额没有超过200， 数量超过10， 折扣为0.85
        
        first_num = second_num = self.money
        if self.money >= 200:
            self._discount = 0.8
            first_num = self.money * self._discount
        if self.goods_count and self.goods_count >= 10:
            self._discount = 0.85
            second_num = self.money * self._discount
        
        if self._discount < 1:
            return 0.8 if first_num < second_num else 0.85
        return self._discount

    def __repr__(self):
        return 'VIP客户'
    

if __name__ == '__main__':
    # 普通客户结账演示
    one_guy = OrdinaryCustomer(50)
    one_guy.check_out()
    two_guy = OrdinaryCustomer(300)
    two_guy.check_out()

    # VIP客户结账演示
    one_richman = VIPCustomer(50)
    one_richman.check_out()
    two_richman = VIPCustomer(100, 10)
    two_richman.check_out()
    three_richman = VIPCustomer(300)
    three_richman.check_out()
    four_richman = VIPCustomer(300, 10)
    four_richman.check_out()
