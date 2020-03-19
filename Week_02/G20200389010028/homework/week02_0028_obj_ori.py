class Person(object):
    def __init__(self):
        self.status = None
        self.price = 0
        self.quantity = 0
        self.pay = 0

    def get_Status(self):
        return self.status

    def get_Price(self):
        return self.price

    def get_Quantity(self):
        return self.quantity


class Vip(Person):
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
        # print('Hi, I am Vip.')

    @property
    def vip_pay(self):
        if self.price >= 200:
            self.pay = self.price * 0.8
        elif self.quantity >= 10:
            self.pay = self.price * 0.85
        else:
            self.pay = self.price
        return self.pay


class Normal(Person):
    def __init__(self, price, quantity):
        super().__init__()
        self.price = price
        self.quantity = quantity
        # print('Ehhh, I am Normal.')

    @property
    def normal_pay(self):
        if self.price >= 200:
            self.pay = self.price * 0.9
        else:
            self.pay = self.price
        return self.pay


class Payment:
    def get_Pay(self, status, price, quantity):
        if status == 'Vip':
            return Vip(price, quantity).vip_pay
        elif status == 'Normal':
            return Normal(price, quantity).normal_pay
        else:
            pass

def main():
    iden = {'A':'Vip', 'B':'Normal'}
    enter = input('如果您是VIP客户请输入A，如果您是普通客户请输入B：')
    pri = float(input('请输入您的购物总额：'))
    quan = int(input('请输入您的购物总件数：'))
    sta = iden[enter]
    payment = Payment()
    pay_final = payment.get_Pay(sta, pri, quan)
    print('您是 %s 客户，您需要付 %.2f 元' % (sta, pay_final))


if __name__ == '__main__':
    main()
