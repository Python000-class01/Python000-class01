class Customer:
    def __init__(self, goods_list):
        self.goods_list = goods_list

    def setPay(self):
        total_price = 0
        total_num = len(self.goods_list)
        for goods in self.goods_list:
            total_price += goods[1]
        return total_price,total_num


class MemBer(Customer):
    def Pay(self):
        price,num = super().setPay()
        if price < 200:
            print(f'{price}')
        else:
            print(f'{price*0.9}')

class VipMember(Customer):
    def Pay(self):
        price,num = super().setPay()
        if num < 10 and price <= 200:
            print(f'{price}')
        elif  num >=10 and price < 200:
            print(f'{price*0.85}')
        else:
            print(f'{price*0.8}')

class Factory:
    def getBrand(self, brand, goods_list):
        if brand == 'normal':
            return MemBer(goods_list).Pay()
        elif brand == 'vip':
            return VipMember(goods_list).Pay()
        else:
            pass


if __name__ == "__main__":
    goods_list = [['test1', 10], ['test2', 200]]

    factory = Factory()
    money = factory.getBrand("vip",goods_list)
