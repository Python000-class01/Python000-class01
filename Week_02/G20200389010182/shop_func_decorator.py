from collections import namedtuple

Customer = namedtuple('Customer', 'name vip')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price   = price

    def total(self):
        return self.price * self.quantity

class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}'
        return fmt.format(self.total(), self.due())

promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def total_price_promo(order):
    if order.customer.vip:
        return order.total() * 0.2 if order.total() >= 200 else 0.0
    else:
        return order.total() * 0.1 if order.total() >= 200 else 0.0

@promotion
def bulk_item_promo(order):
    if order.customer.vip:
        distinct_items = {item.quantity for item in order.cart}
        if sum(distinct_items) >= 10:
            return order.total() * 0.15
        return 0
    return 0

def best_promo(order):
    return max(promo(order) for promo in promos)

# e.g,
joe = Customer('John Doe', 0)
# vip
ann = Customer('Ann Smith', 1)

# > 200 and item > 10
cart3 = [LineItem('banana', 8, 8),
        LineItem('apple', 10, 6),
        LineItem('watermelon', 5, 20)]
# Order(ann, cart3, total_price_promo)
# Order(ann, cart3, bulk_item_promo)
print(Order(ann, cart3, best_promo))

