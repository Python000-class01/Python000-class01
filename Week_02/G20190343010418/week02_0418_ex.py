class Goods(object):
    def __init__(self, price):
        self.price = price


class Consumer(object):
    def __init__(self):
        pass

    def pay(self, list_goods):
        pass

    def total_amount(self, list_goods):
        total_amount = 0.0
        for goods in list_goods:
            total_amount += goods.price
        return total_amount


class CommonConsumer(Consumer):
    def __init__(self):
        pass

    def pay(self, list_goods):
        total_amount = self.total_amount(list_goods)
        if total_amount < 200:
            return total_amount
        else:
            return total_amount * 0.9


class VipConsumer(Consumer):
    def pay(self, list_goods):
        total_amount = self.total_amount(list_goods)
        goods_num = len(list_goods)
        if total_amount < 200:
            if goods_num >= 10:
                return total_amount * 0.85
            else:
                return total_amount
        else:
            return total_amount * 0.8


def convenience_store_996():
    list_goods = [Goods(1), Goods(2), Goods(3), Goods(4), Goods(5)]

    common_consumer = CommonConsumer()
    vip_consumer = VipConsumer()
    total_amount = common_consumer.total_amount(list_goods)
    print(f'total_amount: {total_amount}')
    print(f'common_consumer pay : {common_consumer.pay(list_goods)}')
    print(f'vip_consumer pay : {vip_consumer.pay(list_goods)}')

    print('---------------------------------------------')
    list_goods = [
        Goods(1),
        Goods(2),
        Goods(3),
        Goods(4),
        Goods(5),
        Goods(1),
        Goods(2),
        Goods(3),
        Goods(4),
        Goods(5)]
    total_amount = common_consumer.total_amount(list_goods)
    print(f'total_amount: {total_amount}')
    print(f'common_consumer pay : {common_consumer.pay(list_goods)}')
    print(f'vip_consumer pay : {vip_consumer.pay(list_goods)}')

    print('---------------------------------------------')
    list_goods = [
        Goods(10),
        Goods(20),
        Goods(30),
        Goods(40),
        Goods(50),
        Goods(10),
        Goods(20),
        Goods(30),
        Goods(4),
        Goods(5)]
    total_amount = common_consumer.total_amount(list_goods)
    print(f'total_amount: {total_amount}')
    print(f'common_consumer pay : {common_consumer.pay(list_goods)}')
    print(f'vip_consumer pay : {vip_consumer.pay(list_goods)}')

    print('---------------------------------------------')
    list_goods = [
        Goods(10),
        Goods(20),
        Goods(30),
        Goods(40),
        Goods(5),
        Goods(10),
        Goods(20),
        Goods(30),
        Goods(4),
        Goods(5)]
    total_amount = common_consumer.total_amount(list_goods)
    print(f'total_amount: {total_amount}')
    print(f'common_consumer pay : {common_consumer.pay(list_goods)}')
    print(f'vip_consumer pay : {vip_consumer.pay(list_goods)}')


if __name__ == '__main__':
    convenience_store_996()
