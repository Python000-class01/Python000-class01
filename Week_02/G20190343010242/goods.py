from decimal import Decimal
from utils import Utils


class Goods:
    __slots__ = ['_goods_id', '_name', '_price']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, "_" + key, value)

    def get_id(self):
        return self._goods_id

    def set_id(self, goods_id):
        self._goods_id = goods_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price    
    
    def set_price(self, price):
        self._price = float(round(Decimal(price), 2))

    @staticmethod
    def get_all_goods():
        return [Goods(**g) for g in Utils.get_data("goods.csv")]

    @staticmethod
    def get_goods(goods_id):
        ret = list(filter((lambda g: g.get_id() == goods_id), Goods.get_all_goods()))
        return ret[0] if ret else None
