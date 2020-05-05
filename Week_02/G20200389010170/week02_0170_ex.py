class BaseDiscount(object):
    def __init__(self):
        pass


class NoDiscount(BaseDiscount):
    def calculate(self, order):
        return order.total 
    

class DiscountOnPrice(BaseDiscount):
    def __init__(self, threshold=0, discount=1):
        self.threshold = threshold
        self.discount = discount
    
    def calculate(self, order):
        return order.total if order.total < self.threshold else order.total * self.discount


class DiscountOnCount(BaseDiscount):
    def __init__(self, threshold=0, discount=1):
        self.threshold = threshold
        self.discount = discount 
    
    def calculate(self, order):
        return order.total if order.count < self.threshold else order.total * self.discount


class Customer(object):
    def __init__(self, username, id, vip):
        self.username = username
        self.id = id
        self.vip = vip


class Item(object):
    """"
    Item
    """
    def __init__(self, name, id, count, unit_price):
        self.name = name
        self.id = id
        self.count = count
        self.unit_price = unit_price 
    
    @property
    def total_price(self):
        return self.count * self.unit_price

class Order(object):
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items

    @property
    def total(self):
        return sum([i.total_price for i in self.items])

    @property
    def count(self):
        return len(self.items)


class Payment(object):
    def __init__(self, customer, items, promotions={'vip': [NoDiscount()], 'normal': [NoDiscount()]}):
        self.customer = customer
        self.items = items
        self.promotions = promotions

    def pay(self):
        if self.customer.vip == True:
            balance = Order(self.customer, self.items)
            final_price = min(p.calculate(balance) for p in self.promotions['vip'])
        else:
            balance = Order(self.customer, self.items)
            final_price = min(p.calculate(balance) for p in self.promotions['normal'])
        return final_price


if __name__ == "__main__":
    customer1 = Customer('Ricky', '0170', True)
    items = [
        Item('bed', '1', 2, 50),
        Item('pillow', '2', 1, 100),
        Item('shoes', '3', 1, 100),
        Item('desk', '4', 1, 100)
    ]

    promotions = {
        'vip': [DiscountOnPrice(), DiscountOnCount()],
        'normal': [DiscountOnPrice()]
    }
    pay = Payment(customer1, items, promotions=promotions)

    print(pay.pay())


