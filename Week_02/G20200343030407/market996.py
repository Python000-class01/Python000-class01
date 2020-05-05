def discount(aClass):
    class NewClass(object):
        def __init__(self, args):
            self.wrapped = aClass(args)

        def check(self, goods_list):
            total, count = self.wrapped.check(goods_list)
            if self.wrapped.vip == '1':
                if total >= 200:
                    total = total * 0.8
                else:
                    if count >= 10:
                        total = total * 0.85
            else:
                if total >= 200:
                    total = total * 0.9
            return total, count

    return NewClass


@discount
class User(object):
    def __init__(self, vip):
        self.vip = vip

    @classmethod
    def check(cls, goods_list):
        total = 0
        count = 0
        for goods in goods_list:
            total += goods.price * goods.count
            count += goods.count
        return total, count


class Goods(object):
    def __init__(self, name, price, count):
        self.name = name
        self.price = float(price if price else 0)
        self.count = int(count if count else 0)
