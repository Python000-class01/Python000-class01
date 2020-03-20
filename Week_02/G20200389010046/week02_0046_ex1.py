# Base Customer
class Customer(object):
    def __init__(self,name,dueAmount,quantity):
        self.name = name
        self.dueAmount = dueAmount
        self.quantity = quantity

    def discount(self):
        return self.dueAmount

# Normal Customer definition
class NormalCustomer(Customer):
    def discount(self):
        if self.dueAmount<200:
            return self.dueAmount
        else:
            return self.dueAmount*0.9

# VIP Customer definition
class VipCustomer(Customer):
    def discount(self):
        if self.dueAmount>200:
            self.dueAmount*=0.8
        elif self.quantity>10:
            self.dueAmount*=0.85
        return self.dueAmount


if __name__ == '__main__':

    #Create a virtual customer list
    customerlist = [{'name':'Alice','due':1000,'quantity':9,'vip':False},
                {'name':'Bob','due':150,'quantity':9,'vip':False},
                {'name':'Chris','due':1000,'quantity':9,'vip':True},
                {'name':'David','due':150,'quantity':11,'vip':True}]


    for item in customerlist:
        name = item['name']
        due = item['due']
        quantity = item['quantity']
        vip = item['vip']
        # whether our customer is vip
        customer = (NormalCustomer(name,due,quantity) if vip==False else VipCustomer(name,due,quantity))
        # print(type(customer))
        print('Dear %s, your due is ￥%.2f.' %(customer.name,customer.discount()))