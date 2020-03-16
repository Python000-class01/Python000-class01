from customer_type import CustomerType
from utils import Utils


class Customer:

    __slots__ = ['_customer_id', '_username', '_customer_type']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'customer_type' and value not in [t.value for t in CustomerType]:
                raise Exception("Invalid customer type.")
            setattr(self, "_" + key, value)

    def get_id(self):
        return self._customer_id

    def set_id(self, customer_id):
        self._customer_id = customer_id

    def get_username(self):
        return self._username
    
    def set_username(self, username):
        self._username = username

    def get_customer_type(self):
        return self._customer_type
    
    def set_customer_type(self, customer_type):
        if customer_type not in [t.value for t in CustomerType]:
            raise Exception("Invalid customer type.")
        self._customer_type = customer_type
    
    @staticmethod
    def get_all_customers():
        return [Customer(**c)for c in Utils.get_data("customers.csv")]

    @staticmethod
    def get_customer(customer_id):
        ret = list(filter((lambda c: c.get_id() == customer_id), Customer.get_all_customers()))
        return ret[0] if ret else None

    @staticmethod
    def get_customer_by_username(username):
        ret = list(filter((lambda c: c.get_username() == username), Customer.get_all_customers()))
        return ret[0] if ret else None