"""
996便利店
简单工厂模式、类的继承、@property
"""


class Convenience_store(object):
    def get_customer_level(self, name, level, total_price, num):
        if level == 'common':
            return Common_customer(name, total_price, num)
        if level == 'vip':
            return Vip_customer(name, total_price, num)


class Customer(object):
    def __init__(self, name, total_price, num):
        self.name = name
        self.num = num
        self.bill = total_price


class Check_out_method(object):
    def __init__(self, name):
        self.name = name

    def common_check_out_method_1(self):
        print(f"{self.name}'s bill is ¥{self.bill:.2f}")

    def common_check_out_method_2(self):
        self.bill = self.bill * 0.9
        print(f"{self.name}'s bill is ¥{self.bill:.2f}")

    def vip_check_out_method_1(self):
        print(f"{self.name}'s bill is ¥{self.bill:.2f}")

    def vip_check_out_method_2(self):
        self.bill = self.bill * 0.85
        print(f"{self.name}'s bill is ¥{self.bill:.2f}")

    def vip_check_out_method_3(self):
        self.bill = self.bill * 0.8
        print(f"{self.name}'s bill is ¥{self.bill:.2f}")

    def vip_check_out_method_4(self):
        bill_num = self.bill * 0.85
        bill_200 = self.bill * 0.8
        if bill_num >= bill_200:
            print(f"{self.name}'s bill is ¥{bill_200:.2f}")
        else:
            print(f"{self.name}'s bill is ¥{bill_num:.2f}")


class Common_customer(Customer, Check_out_method):
    def __init__(self, name, total_price, num):
        super().__init__(name, total_price, num)

    @property
    def check_out(self):
        if self.bill >= 200:
            return self.common_check_out_method_2()
        return self.common_check_out_method_1()


class Vip_customer(Customer, Check_out_method):
    def __init__(self, name, total_price, num):
        super().__init__(name, total_price, num)

    @property
    def check_out(self):
        if self.num >= 10 and self.bill < 200:
            return self.vip_check_out_method_2()
        elif self.num < 10 and self.bill >= 200:
            return self.vip_check_out_method_3()
        elif self.num >= 10 and self.bill >= 200:
            return self.vip_check_out_method_4()
        return self.vip_check_out_method_1()


def customer_info():
    name = input("Please enter customer's name: ")
    while True:
        level = input("Please enter customer's' level ('vip' or 'common'): ")
        if level == 'vip' or level == 'common':
            break
        print("Your input is incorrect, please try again.")
    while True:
        try:
            total_price = float(input("Please enter total_price: "))
            break
        except ValueError:
            print("Your input is not a price, please try again.")
    while True:
        try:
            num = int(input("Please enter goods number: "))
            break
        except ValueError:
            print("Your input is not a number, please try again. ")
    return name, level, total_price, num


if __name__ == '__main__':
    shop_996 = Convenience_store()
    info = customer_info()
    customer = shop_996.get_customer_level(info[0], info[1], info[2], info[3])
    customer.check_out