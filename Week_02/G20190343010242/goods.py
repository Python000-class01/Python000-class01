from decimal import Decimal
from utils import Utils


class Goods:
    __slots__ = ['__goods_id', '__name', '__price']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, "_Goods__" + key, value)

    def get_id(self):
        return self.__goods_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price    
    
    def set_price(self, price):
        self.__price = float(round(Decimal(price), 2))

    @staticmethod
    def get_all_goods():
        return [Goods(**g) for g in Utils.get_data("goods.csv")]

    @staticmethod
    def get_goods(goods_id):
        ret = list(filter((lambda g: g.get_id() == goods_id), Goods.get_all_goods()))
        return ret[0] if ret else None
