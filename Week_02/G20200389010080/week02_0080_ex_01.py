import random

class Cashier(object):
    def checkout(self, customer):
        amount_to_pay, number_of_item = customer.payment()
        print('You purchased %5d items, need to pay %5.2d' % (number_of_item, amount_to_pay))
        final_bills = 0
        if customer.status == 'normal':
            final_bills = self.normal_payment(amount_to_pay)
        elif customer.status == 'vip':
            final_bills = self.vip_payment(amount_to_pay, number_of_item)
        print('please pay: %8.2d' % final_bills)

    def normal_payment(self, amount_to_pay):
        print('ooops! you are too normal')
        if amount_to_pay < 200:
            print('no discount since your bill is less than 200')
            return amount_to_pay
        else:
            print('10% off')
            return amount_to_pay * 0.9


    def vip_payment(self, amount_to_pay, number_of_item):
        print('oh! you are my VIP')
        if amount_to_pay >= 200:
            print('20% off')
            return amount_to_pay * 0.8
        elif number_of_item >= 10:
            print("15% off")
            return amount_to_pay * 0.85
        else:
            print('no discount since your bill is less than 200')
            return amount_to_pay

class Customer(object):
    def __init__(self, status):
        self.status = status
    def payment(self):
        amount_to_pay = random.uniform(1,3) * 100
        number_of_item = random.randint(1,15)
        return amount_to_pay, number_of_item
if __name__ == "__main__":
    customer_status = ['normal', 'vip']
    cashier = Cashier()
    for i in range(1,10):
        print('process customer # %s' % i)
        print('-------------------------')
        current_status = random.choice(customer_status)
        current_customer = Customer(current_status)
        cashier.checkout(current_customer)
        print('\n')