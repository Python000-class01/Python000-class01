

#定义商品单价
goods = {
    'mian':5,
    'beer':10,
    'meat':100,
}

#购物车
def add_list():
    print("这是我们的商品以及价格：",goods)
    shop_list = []
    while True:
        good_name = input("请输入需要购买的商品:")
        good_num = input("请输入购买的数量：")
        shop_list.append([good_name,good_num])
        jixu = input("请问还需要其他产品吗?(y/n)")
        if jixu == "n":
            break
    return shop_list




#价格预处理
def pre_price():
    shop_lanzi = add_list()
    pre_sum_price = 0
    nums = 0
    for i in shop_lanzi:
        price = int(int(goods[i[0]]) * int(i[1]))
        nums += int(i[1])
        pre_sum_price += price
    return  pre_sum_price,nums



def jiesuan():
    vip = input("请问您是否是VIP？(y/n)")
    init_price = pre_price()[0]
    if vip == 'y':
        if init_price >= 200:
            z_price = init_price * 0.8
            return z_price
        elif init_price <200 and init_price >= 10:
            z_price = init_price * 0.85
            return z_price
        else:
            z_price = init_price
            return z_price
    elif vip == 'n':
        if init_price >= 200:
            z_price = init_price * 0.9
            return z_price
        else:
            z_price = init_price
            return z_price






if __name__ ==  "__main__":
    print("welcoome to 996 shop!!!")
    print("您应付：",jiesuan())













