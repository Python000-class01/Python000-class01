import random


totalItem = {}
totalItem['iphone_7_64'] = 1
totalItem['iphone_7_128'] = 5
totalItem['iphone_7_256'] = 10
totalItem['iphone_7_plus_64'] = 6
totalItem['iphone_7_plus_128'] = 11
totalItem['iphone_7_plus_256'] = 16
totalItem['iphone_8_64'] = 3
totalItem['iphone_8_128'] = 8
totalItem['iphone_8_256'] = 13
totalItem['iphone_8_plus_64'] = 8
totalItem['iphone_8_plus_128'] = 13
totalItem['iphone_8_plus_256'] = 18
totalItem['iphone_xr_64'] = 20
totalItem['iphone_xr_128'] = 30
totalItem['iphone_xr_256'] = 40
totalItem['iphone11_64'] = 50
totalItem['iphone11_128'] = 60
totalItem['iphone11_256'] = 70
totalItem['iphone11_pro_64'] = 80
totalItem['iphone11_pro_128'] = 90
totalItem['iphone11_pro_256'] = 100
totalItem['iphone11_Pro_max_64'] = 110
totalItem['iphone11_pro_max_128'] = 120
totalItem['iphone11_pro_max_256'] = 130
totalItem['xiaomi10_128'] = 140
totalItem['xiaomi10_256'] = 150
totalItem['xiaomi10_pro_128'] = 160
totalItem['xiaomi10_pro_256'] = 180


class User:
    def __init__(self, name, rank, cart={}):
        self._name = name
        self._rank = rank
        self._cart = cart

    @property
    def name(self):
        return self._name

    @property
    def rank(self):
        return self._rank

    @property
    def cart(self):
        return self._cart

    @cart.setter
    def cart(self, value):
        self._cart = value


def get_order_cost(user):
    item_count = 0
    rank = user.rank
    cost = 0
    for item in user.cart.values():
        item_count += item
    print("商品数量:" + str(item_count))
    for item in user.cart.keys():
        cost += totalItem[item] * user.cart[item]
    print("原价:" + str(cost))
    discount_cost = cost
    discount_infos = ["无折扣", "普通用户满200九折", "vip满200八折", "vip满十件85折"]
    discount_info = discount_infos[0]
    if rank == 0:
        if cost >= 200:
            discount_cost = (cost * 0.9)
            discount_info = discount_infos[1]
    elif (cost >= 200) or (item_count >= 10):

        discount_cost1 = cost
        discount_cost2 = cost
        if cost >= 200:
            discount_cost1 = (cost * 0.8)
        if item_count >= 10:
            discount_cost2 = (cost * 0.85)

        if discount_cost1 < discount_cost2:
            discount_cost = discount_cost1
            discount_info = discount_infos[2]
        else:
            discount_cost = discount_cost2
            discount_info = discount_infos[3]
    print("折后价:" + str(discount_cost))
    print("优惠策略:" + str(discount_info))
    return discount_cost


# 生成测试用户实例，并随机生成item_count3件商品，商品类型可能重复，即一件商品购买 多件
def mock_user_buy_item(name, rank, item_count):
    _user = User(name, rank)
    cart = {}
    items = list(totalItem.keys())
    for i in range(0, item_count):
        item_index = random.randint(0, len(items)-1)
        item_name = items[item_index]
        if item_name in cart:
            cart[item_name] = cart[item_name] + 1
        else:
            cart[item_name] = 1
    _user.cart = cart
    return _user


if __name__ == '__main__':
    # normal_user = User("jack", 0)

    # vip_user = User("tom", 1)
    # vip_user2 = User("micky", 1)
    # print(str(totalItem))
    # for i in range(0, 10):
    #     print(random.randint(0, 3))
    # 普通用户
    user1 = mock_user_buy_item('jack', 0, 4)
    print(user1.cart)
    print(get_order_cost(user1))

    user2 = mock_user_buy_item('jack2', 0, 10)
    print(user2.cart)
    print(get_order_cost(user2))

    user3 = mock_user_buy_item('jack2', 0, 11)
    print(user3.cart)
    print(get_order_cost(user3))

    # vip用户
    user4 = mock_user_buy_item('jack', 1, 4)
    print(user4.cart)
    print(get_order_cost(user4))

    user5 = mock_user_buy_item('jack2', 1, 10)
    print(user5.cart)
    print(get_order_cost(user5))

    user6= mock_user_buy_item('jack2', 1, 11)
    print(user6.cart)
    print(get_order_cost(user6))
