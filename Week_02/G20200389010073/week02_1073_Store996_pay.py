#region 作业要求
# 作业一：
# 为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：
# 1.普通用户消费不足 200 元，无折扣，原价付费；
# 2.普通用户消费满 200 元打九折；
# 3.VIP 会员满 200 元打八折；
# 4.VIP 会员满 10 件商品打八五折。
# 要求：
# 1.请使用面向对象编程实现结算功能。
# 2.由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。
#endregion


def Get_pay_Info(func):
    """装饰器：pay（）拓展功能：获取付款信息：总金额，商品个数"""
    def inner(self):
        int_goodnumber = 0
        for onegood in self.list_goods:
            int_goodnumber = int_goodnumber + onegood['int_good_number']
        double_paymentamount = func(self)
        print(
            f'付款信息：\n>>> 应收金额：{double_paymentamount}\n>>> 商品总数：{int_goodnumber}\n'
        )
        dict_payment = {
            'double_paymentamount': double_paymentamount,
            'int_goodnumber': int_goodnumber
        }
        return dict_payment

    return inner


class Payment_Module(object):
    """ 付款基础类 """
    def __init__(self, str_customer_name):
        self.int_payment_amount = 0
        self.list_goods = []
        self.str_customer_name = str_customer_name

    def Input_Good(self,
                   str_good_name,
                   double_good_price=0,
                   int_good_number=0):
        """ 录入商品（商品名称，商品单价，商品数量） """
        dict_one_good = {
            'str_good_name': str_good_name,
            'double_good_price': double_good_price,
            'int_good_number': int_good_number,
            'double_good_amount': (double_good_price * int_good_number)
        }
        self.list_goods.append(dict_one_good)
        print(f'已录入购买商品信息：\n' + f'>>> 名称：{str_good_name}\n' +
              f'>>> 单价：{double_good_price}\n' + f'>>> 数量：{int_good_number}\n' +
              f'>>> 总价：{(double_good_price * int_good_number)}\n')

    @Get_pay_Info
    def pay(self):
        """ 获取付款金额 """
        for one_good in self.list_goods:
            self.int_payment_amount = self.int_payment_amount + one_good[
                'double_good_amount']
        return self.int_payment_amount


def Get_Discount_Customer_VIP(func):
    """ 计算优惠价格 """
    def inner(self):
        dict_payment = func(self)
        double_paymentamount = dict_payment['double_paymentamount']
        int_goodnumber = dict_payment['int_goodnumber']
        double_payment_discount_1 = 0
        double_payment_discount_2 = 0
        if double_paymentamount >= 200:
            double_payment_discount_1 = double_paymentamount * .8

        if int_goodnumber >= 10:
            double_payment_discount_2 = double_paymentamount * .85

        if double_payment_discount_1 > double_payment_discount_2 and double_payment_discount_2 != 0:
            print(
                f'VIP客户：{self.str_customer_name}\n' +
                f'>>> 原价付款：{double_paymentamount}\n' + f'享受<八八五折优惠>后付款信息：\n' +
                f'>>> 应收金额：{double_payment_discount_2}\n>>> 商品总数：{int_goodnumber}\n'
            )
            double_paymentamount = double_payment_discount_2

        elif double_payment_discount_1 < double_payment_discount_2 and double_payment_discount_1 == 0:
            print(
                f'VIP客户：{self.str_customer_name}\n' +
                f'>>> 原价付款：{double_paymentamount}\n' + f'享受<八八五折优惠>后付款信息：\n' +
                f'>>> 应收金额：{double_payment_discount_2}\n>>> 商品总数：{int_goodnumber}\n'
            )
            double_paymentamount = double_payment_discount_2

        elif double_payment_discount_1 < double_payment_discount_2 and double_payment_discount_1 != 0:
            print(
                f'VIP客户：{self.str_customer_name}\n' +
                f'>>> 原价付款：{double_paymentamount}\n' + f'享受<八折优惠>后付款信息：\n' +
                f'>>> 应收金额：{double_payment_discount_1}\n>>> 商品总数：{int_goodnumber}\n'
            )
            double_paymentamount = double_payment_discount_1

        elif double_payment_discount_1 > double_payment_discount_2 and double_payment_discount_2 == 0:
            print(
                f'VIP客户：{self.str_customer_name}\n' +
                f'>>> 原价付款：{double_paymentamount}\n' + f'享受<八折优惠>后付款信息：\n' +
                f'>>> 应收金额：{double_payment_discount_1}\n>>> 商品总数：{int_goodnumber}\n'
            )
            double_paymentamount = double_payment_discount_1

    return inner


class Customer_VIP(Payment_Module):
    """ VIP客户 """
    def __init__(self, str_customer_name):
        super().__init__(str_customer_name)
        print(f'Customer_VIP:{str_customer_name}')

    @Get_Discount_Customer_VIP
    def pay(self):
        return super().pay()


def Get_Discount_Customer_Nomal(func):
    """ 计算优惠价格 """
    def inner(self):
        dict_payment = func(self)
        double_paymentamount = dict_payment['double_paymentamount']
        int_goodnumber = dict_payment['int_goodnumber']
        if double_paymentamount >= 200:
            double_payment_discount_2 = double_paymentamount * .9
            print(
                f'普通客户：{self.str_customer_name}\n' +
                f'>>> 原价付款：{double_paymentamount}\n' + f'享受<九折优惠>后付款信息：\n' +
                f'>>> 应收金额：{double_payment_discount_2}\n>>> 商品总数：{int_goodnumber}\n'
            )
            double_paymentamount = double_payment_discount_2

    return inner


class Customer_Nomal(Payment_Module):
    """ 普通客户 """
    def __init__(self, str_customer_name):
        super().__init__(str_customer_name)
        print(f'Customer_Nomal:{str_customer_name}')

    @Get_Discount_Customer_Nomal
    def pay(self):
        return super().pay()


class Factory(object):
    """ 工厂 """
    def create_customer(self, str_customer_name, str_customer_level):
        if str_customer_level == 'VIP':
            return Customer_VIP(str_customer_name)
        else:
            return Customer_Nomal(str_customer_name)


if __name__ == '__main__':

    C_factory = Factory()
    
    c = C_factory.create_customer("Jone", "Nomal")
    c.Input_Good('Good_3', 10, 20)
    c.pay()

    d = C_factory.create_customer("Peter", "VIP")
    d.Input_Good('Good_3', 10, 20)
    d.pay()