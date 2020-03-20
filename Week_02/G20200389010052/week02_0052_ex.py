'''
为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：

普通用户消费不足 200 元，无折扣，原价付费；
普通用户消费满 200 元打九折；
VIP 会员满 200 元打八折；
VIP 会员满 10 件商品打八五折。
要求：

请使用面向对象编程实现结算功能。
由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。
'''


# 顾客
class user(object):
    def __init__(self, name):
        self.name = name

    def shopping(self, goods, num):
        # for range(num):
        # shoppingCart.append(goods)
        pass


class vip_user(user):
    vipflag = True


class general_user(user):
    vipflag = False


# 商品
class goods(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def __str__(self):
        info = '商品名称：%s 商品价格：%s' % (self.name, self.price)
        print(info)


# 超市
class supermarket(object):
    def __init__(self, name):
        self.name = name
        self.goods = [{'name': '西瓜', 'price': '20'},
                      {'name': '笔记本', 'price': '10'},
                      {'name': '香烟', 'price': '5'},
                      {'name': '辣条', 'price': '15'},
                      {'name': '手机', 'price': '500'}]
        print('欢迎光临%s超市' % self.name)
        i = 0
        for gd in self.goods:
            print('商品编号【%s】商品名称【%s】商品价格【%s】' % (i, gd.get('name'), gd.get('price')))
            i += 1

    # 支付
    def pay(self, list_goods=None, vipflag=False):
        # 支付结算
        total = 0
        count = 0
        for gd in list_goods:
            total += int(gd.get('goods').price) * int(gd.get('num'))
            count += int(gd.get('num'))
        # 计算折扣
        if vipflag:
            if total > 200:
                total *= 0.8
                print('VIP 会员满 200 元打八折，实付金额：%s' % total)
            elif count > 10:
                total *= 0.85
                print('VIP 会员满 10 件商品打八五折，实付金额：%s' % total)
        elif total > 200:
            total *= 0.9
            print('普通用户消费满 200 元打九折，实付金额：%s' % total)
        else:
            print('无折扣，实付金额：%s' % total)

    # 购买商品
    def shopping(self, list_goods=None):
        while 1:
            input_ = input("请输入你要购买商品的编号及数量，用','分开:")
            str_list = input_.split(',')
            number = int(str_list[0])
            count = int(str_list[1])
            gd = self.goods[number]
            goods_ = goods(gd.get('name'), gd.get('price'))
            list_goods.append({'goods': goods_, 'num': count})
            print('%s * %s 已经成功加入购物车' % (gd.get('name'), count))
            input_ = input('是否继续购物? Y/N:')
            if input_ == 'Y':
                continue
            else:
                break
        return list_goods


if __name__ == '__main__':
    sp = supermarket('996')
    list_goods = []
    user1 = vip_user('小红')
    list_goods = sp.shopping(list_goods)
    sp.pay(list_goods, user1.vipflag)

    list_goods2 = []
    user2 = general_user('小绿')
    list_goods = sp.shopping(list_goods2)
    sp.pay(list_goods2, user2.vipflag)
