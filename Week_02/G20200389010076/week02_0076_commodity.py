class Commodity(object):
    def __init__(self,cmdy_name,cmdy_price):
        self._name=cmdy_name
        self._price=cmdy_price
        # self._number=cmdy_number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,cmdy_name):
        self._name=cmdy_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,cmdy_price):
        self._price=cmdy_price



class Kola(Commodity):
    def __init__(self):
        super().__init__('可乐',35.0)


class Sprite(Commodity):
    def __init__(self):
        super().__init__('雪碧',25.0)


class Biscuits(Commodity):
    def __init__(self):
        super().__init__('饼干',90.0)


