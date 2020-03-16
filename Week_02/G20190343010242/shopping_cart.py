from customer import Customer
from goods import Goods
from customer_type import CustomerType
from configure import getConfig
from utils import Utils
from decimal import Decimal
from prettytable import PrettyTable


class ShoppingCart:

    def __init__(self, customer_id):
        super().__init__()
        self._customer_id = customer_id
        self._customer = Customer.get_customer(customer_id)
        if not self._customer:
            raise Exception("Customer is not found.")
        self.vip_discount = float(getConfig().get('vip_discount', '0.8'))
        self.vip_threshold = float(getConfig().get('vip_threshold', '200.0'))
        self.vip_item_threshold = int(getConfig().get('vip_item_threshold', '10'))
        self.vip_item_discount = float(getConfig().get('vip_item_discount', '0.85'))
        self.generic_discount = float(getConfig().get('generic_discount', '0.9'))
        self.generic_threshold = float(getConfig().get('generic_threshold', '200.0'))
    
    def get_customer_id(self):
        return self._customer_id

    def get_customer(self):
        return self._customer
    
    def get_order_entries(self):
        all_entries = [self.OrderEntry(**oe) for oe in Utils.get_data("order_entries.csv")]
        return list(filter((lambda oe : oe.customer_id == self._customer_id), all_entries))

    def get_total_price(self):
        total_qty = 0
        total_price = 0.0
        discount = 0.0
        for order_entry in self.get_order_entries():
            total_qty += order_entry.qty
            goods = Goods.get_goods(order_entry.goods_id)
            total_price += goods.get_price() * order_entry.qty
        # Discounts
        if self._customer.get_customer_type() == CustomerType.GENERIC.value:
            if total_price >= self.generic_threshold:
                total_price = total_price * self.generic_discount
                discount = float(round(Decimal(1.0 - self.generic_discount), 2))
        elif self._customer.get_customer_type() == CustomerType.VIP.value:
            if total_price >= self.vip_threshold:
                total_price = total_price * self.vip_discount
                discount = float(round(Decimal(1.0 - self.vip_discount), 2))
            elif total_qty >= self.vip_item_threshold:
                total_price = total_price * (self.vip_discount if total_price >= self.vip_threshold else self.vip_item_discount)
                discount = float(round(Decimal(1.0 - (self.vip_discount if total_price >= self.vip_threshold else self.vip_item_discount)), 2))
        return total_price, discount

    def print_orders(self):
        user_category = "VIP" if self._customer.get_customer_type() == CustomerType.VIP.value else "Generic"
        print(f"***** Orders for User {self._customer.get_username()}, User category: {user_category} *****")
        print()
        t = PrettyTable(['Goods Code', 'Goods Name', 'Unit Price', 'Qty'])
        for entry in self.get_order_entries():
            goods = Goods.get_goods(entry.goods_id)
            t.add_row([goods.get_id(), goods.get_name(), Utils.printed_currency(goods.get_price()), entry.qty])
        print(t)
        print()
        print()
        total_price, discount = self.get_total_price()
        if discount > 0.0:
            print(f"Discount:  {int(discount * 100)}% off")
        print(f"Total price: {Utils.printed_currency(total_price)}")

    class OrderEntry:

        __slots__ = ['customer_id', 'goods_id', 'qty']

        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

