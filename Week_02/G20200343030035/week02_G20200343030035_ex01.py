
# 客人 （原总价、商品数）
class Cus_Pay(object):
    def __init__(self, original_pay, quantity):
        self._original_pay = original_pay
        self._quantity = quantity

    def pay(self):
        return self._original_pay

class Normal_Cus_Pay(Cus_Pay):
    def __init__(self, original_pay, quantity):
        super().__init__(original_pay, quantity)

    def pay(self):
        if self._original_pay < 200:
            return self._original_pay
        else:
            return self._original_pay * 0.9    

class Vip_Cus_pay(Cus_Pay):
    def __init__(self, original_pay, quantity):
        super().__init__(original_pay, quantity)
    
    def pay(self):
        if self._original_pay >= 200:
            return self._original_pay * 0.8
        elif self._quantity >= 10:
            return self._original_pay * 0.85

if __name__ == '__main__':
    true_cus1 = {'vip':True, 'original_pay':1000, 'quantity':13}
    if true_cus1['vip'] == True:
        print(f'Dear vip, your payment will be: {Vip_Cus_pay(true_cus1["original_pay"], true_cus1["quantity"]).pay()}')
    else:
        print(f'Dear customer, your payment will be: {Normal_Cus_pay(true_cus1["original_pay"], true_cus1["quantity"]).pay()}')


