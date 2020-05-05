from dataclasses import dataclass
from collections.abc import Iterable
from abc import abstractmethod


@dataclass
class Product:
    name: str
    price: float

class Discount:
    @abstractmethod
    def get_discounted_bill(self, product_num, total_bill) -> int:
        pass

# 满200打九折
class Normal200BillDiscount(Discount):
    def get_discounted_bill(self, product_num, total_bill) -> int:
        return total_bill * 0.9 if total_bill >= 200 else total_bill

# vip满200打8折
class Vip200BillDiscount(Discount):
    def get_discounted_bill(self, product_num, total_bill) -> int:
        return total_bill * 0.8 if total_bill >= 200 else total_bill

# vip满10件打85折
class Vip10ProductsDiscount(Discount):
    def get_discounted_bill(self, product_num, total_bill) -> int:
        return total_bill * 0.85 if product_num >= 10 else total_bill

def vip_wrapper(cls):
    class inner(cls):
        def __init__(self):
            super().__init__()
            self.add_discount_method(Vip200BillDiscount())
            self.add_discount_method(Vip10ProductsDiscount())

    return inner

def normal_wrapper(cls):
    class inner(cls):
        def __init__(self):
            super().__init__()
            self.add_discount_method(Normal200BillDiscount())

    return inner


class Customer:
    def __init__(self):
        self.products = []
        self.__discount_methods = []

    def add_discount_method(self, func):
        self.__discount_methods.append(func)

    def buy_product(self, products):
        if isinstance(products, Iterable):
            self.products.extend(products)
        else:
            self.products.append(products)

    def pay_bill(self):
        product_num, total_bill = len(self.products), sum([x.price for x in self.products])
        ans = total_bill
        for discount in self.__discount_methods:
            ans = min(ans, discount.get_discounted_bill(product_num, total_bill))
        print(f'Customer payed ${ans} for products:\n{self.products}')
        self.products = []

@vip_wrapper
class VipCustomer(Customer):
    pass

@normal_wrapper
class NormalCustomer(Customer):
    pass

if __name__ == '__main__':
    customer1 = NormalCustomer()
    customer2 = VipCustomer()

    # 触发普通用户满200打9折
    customer1.buy_product([Product(f'product{i}', 100) for i in range(4)])
    customer1.pay_bill()

    # 触发普通用户不打折
    customer1.buy_product([Product(f'product{i}', 25) for i in range(4)])
    customer1.pay_bill()

    # 触发vip用户满200打8折
    customer2.buy_product([Product(f'product{i}', 100) for i in range(4)])
    customer2.pay_bill()

    # 触发vip用户满10件打85折
    customer2.buy_product([Product(f'product{i}', 10) for i in range(10)])
    customer2.pay_bill()

    # 触发vip用户同时满足满10件和满200元，选最多折扣8折
    customer2.buy_product([Product(f'product{i}', 20) for i in range(10)])
    customer2.pay_bill()

    # 触发vip用户不打折
    customer2.buy_product([Product(f'product{i}', 25) for i in range(4)])
    customer2.pay_bill()
