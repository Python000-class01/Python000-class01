import sys
from customer import Customer
from shopping_cart import ShoppingCart

args = sys.argv
if len(args) != 2:
    raise Exception("Invalid argument.")
username = args[1]
try:
    customer = Customer.get_customer_by_username(username)
    if not customer:
        raise Exception("Customer is not found.")
    shopping_cart = ShoppingCart(customer.get_id())
    shopping_cart.print_orders()
except Exception as e:
    print(e)