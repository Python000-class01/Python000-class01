
class Customer:
    def __init__(self, goods_numes, all_pay, is_vip=False):
        self.is_vip = is_vip
        self.goods_numes = goods_numes
        self.all_pay = all_pay

    def final_pay(self):
        if self.is_vip:
            if self.all_pay >= 200:
                print("VIP客户，满足金额达标折扣！")
                self.final_pay = self.all_pay*0.8
            elif self.goods_numes >= 10:
                print("VIP客户，满足数量达标折扣！")
                self.final_pay = self.all_pay*0.85
            else:
                print("VIP客户，不满足折扣条件！")
                self.final_pay = self.all_pay
        else:
            if self.all_pay >= 200:
                print("非VIP客户，满足金额达标折扣！")
                self.final_pay = self.all_pay * 0.9
            else:
                print("非VIP客户，不满足折扣条件！")
                self.final_pay = self.all_pay
        return self.final_pay


if __name__ == "__main__":
    cust1 = Customer(20, 220)
    print("您需要支付: {}元！".format(cust1.final_pay()))
    cust2 = Customer(8, 200, True)
    print("您需要支付: {}元！".format(cust2.final_pay()))
    cust3 = Customer(10, 180, True)
    print("您需要支付: {}元！".format(cust3.final_pay()))
    cust4 = Customer(8, 180, True)
    print("您需要支付: {}元！".format(cust4.final_pay()))