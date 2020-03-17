class A(object):
    total_money = 1
    total_goods = 3

    def __init__(self, goods = None):
        if goods is None:
            self.goods = []

class B(A):
    def test(self):
        print(A.total_goods)
        print(A.total_money)











