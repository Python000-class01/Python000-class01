import functools

class DiscountManager:

    def __init__(self):
        self.discounts = []

    def discount_register(self, func):
        print("Add ", func.__name__, " into discounts")  
        self.discounts.append(func)
        @functools.wraps(func)
        def calc_discount(*args, **kwargs):                   
            return func(*args, **kwargs)
        return calc_discount



dm = DiscountManager()

@dm.discount_register
def common_pay_full_200_discount(isvip, pay, quantity):
    '''普通用户满200打9折'''
    disc = 1
    if isvip == False and pay >= 200:
        disc = 0.9
    print(f'common_pay_full_200_discount policy discount is {disc:.2f}')
    return disc

@dm.discount_register
def vip_pay_full_200_discount(isvip, pay, quantity):
    '''vip用户满200打8折'''
    disc = 1
    if isvip == True and pay >= 200:
        disc = 0.8
    print(f'vip_pay_full_200_discount policy discount is {disc:.2f}')
    return disc

@dm.discount_register
def vip_quantity_full_10_discount(isvip, pay, quantity):
    '''vip用户满10件打85折'''
    disc = 1
    if isvip == True and quantity >= 10:
        disc = 0.85
    print(f'vip_quantity_full_10_discount policy discount is {disc:.2f}')
    return disc 