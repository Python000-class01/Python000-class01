import random

class Goods(object):
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return "id:{},name:{},price{}".format(str(self.id), self.name, str(self.price))


class Consumer(object):
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        # 0-普通用户 1-VIP
        self.type = type

    def __str__(self):
        return "id:{},name:{},type:{}".format(str(self.id), self.name, str(self.type))


class ShopManager(object):
    def __init__(self, consumer, goods_list):
        self.consumer = consumer
        self.goods_list = goods_list

    def pay(self):
        print(self.consumer)
        for goods in goods_list:
            print(goods)
        total_price = 0
        total_num = len(self.goods_list)
        for goods in self.goods_list:
            total_price += goods.price

        print(total_price)

        if self.consumer.type == 0:
            if total_price < 200:
                return total_price
            else:
                return total_price * 0.9
        elif self.consumer.type == 1:
            if total_price < 200 and total_num < 10:
                return total_price
            elif total_price < 200 and total_num >= 10:
                return total_price * 0.85
            else:
                return total_price * 0.8


if __name__ == '__main__':
    consumer = Consumer(1, 'zhangsan', 1)
    goods_list = []
    for i in range(10):
        goods_list.append(Goods(i, 'goods' + str(i), round(random.uniform(10, 30), 2)))

    shopManager = ShopManager(consumer, goods_list)
    total = shopManager.pay()
    print(total)
