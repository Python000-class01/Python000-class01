from collections import namedtuple

Customer = namedtuple('Customer', 'name mobile')
Product  = namedtuple('Product', 'name qy')      #qy代表数量

class Order:

    def __init__(self, customer, cart=None):
        self.customer = customer
        
        assert cart is not None, f'This order does not have Cart information...'
        self.cart = list(cart)

    #def __repr__(self):
    #    info = f'Order - Customer: {}, order: {}', self.customer.name, self.cart
    #    print(info)
    