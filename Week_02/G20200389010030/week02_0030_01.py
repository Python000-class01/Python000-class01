class TypeDes(object):
    """
    类型检查描述符
    """
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        del instance.__dict__[self.name]

def TypeCheck(**kwargs):
    """
    类装饰器
    """
    def decorate(cls):
        for name, expected_type in kwargs.items():
            setattr(cls, name, TypeDes(name, expected_type))
        return cls
    return decorate

@TypeCheck(name=str, price=float)
class Goods(object):
    """
    商品类
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

@TypeCheck(name=str, isvip=bool)
class Customer(object):
    """
    消费者类
    """
    def __init__(self, name, isvip):
        self.name = name
        self.isvip = isvip
        self.goods_cart = []

    def buy_goods(self, goods):
        self.goods_cart.append(goods)

    @property
    def consumption(self):
        sum_price = 0
        for goods in self.goods_cart:
            sum_price += goods.price
        
        if not self.isvip:
            return sum_price if sum_price < 200 else sum_price * 0.9
        
        if sum_price >= 200:
            return sum_price * 0.8
        elif len(self.goods_cart) >= 10:
            return sum_price * 0.85
        else:
            return sum_price

        
if __name__ == "__main__":
    # 实例化商品
    apple = Goods("apple", 10.0)
    orange = Goods("orange", 20.0)
    shoes = Goods("shoes", 200.0)
    # 实例化消费者
    c1 = Customer("c1", True)
    c2 = Customer("c2", False)
    # 消费者购买商品
    c1.buy_goods(apple)
    c1.buy_goods(shoes)
    c2.buy_goods(orange)
    c2.buy_goods(shoes)
    # 计算消费金额
    print(c1.consumption)
    print(c2.consumption)

