import pandas as pd


class User:

    def __init__(self, name, is_vip=0):
        self.name = name
        self.is_vip = is_vip
        self.cart = []
        self.cart_price = 0

    def buy(self, goods):
        self.cart.append(goods)

    def cart_goods(self):
        return self.cart

    def pay(self):
        if self.is_vip == 1:
            print('尊敬的vip客户')
            pay_money = self.cart_price

            '''
            VIP 会员满 200 元打八折；
            VIP 会员满 10 件商品打八五折。
            '''

            # 大于200并且大于10件商品
            if self.cart_price >= 200 and len(self.cart) >= 10:
                pay_money_1 = self.cart_price * 0.8
                pay_money_2 = self.cart_price * 0.85
                if pay_money_1 > pay_money_2:
                    pay_money = pay_money_2
                else:
                    pay_money = pay_money_1
                print('大于200 大于10 件')
            elif self.cart_price >= 200 and len(self.cart) < 10:
                pay_money = self.cart_price * 0.8
                print('大于200 小于10件 8折')
            elif self.cart_price < 200 and len(self.cart) >= 10:
                pay_money = self.cart_price * 0.85
                print('小于200 大于10 件 85折')
            else:
                print('小于200 小于10 件')
                pass
        else:
            print('我连vip都不是')
            # 如果满200元打九折，否则无折扣
            pay_money = self.cart_price
            if self.cart_price >= 200:
                pay_money = self.cart_price * 0.9

        print('实际支付：' + str(pay_money))


class Goods:

    def goods_list(self):
        goods_list = [
            {'name': 'Python基础', 'price': '9.20', 'author': '一位不愿意透漏姓名的网友'},
            {'name': 'Mysql入门', 'price': '21.80', 'author': '一位不愿意透漏姓名的网友'},
            {'name': 'Linux运维', 'price': '34.50', 'author': '一位不愿意透漏姓名的网友'},
            {'name': 'Python从入门到放弃', 'price': '21.20', 'author': '一位不愿意透漏姓名的网友'},
            {'name': 'Mysql从删库导跑路', 'price': '24.20', 'author': '一位不愿意透漏姓名的网友'},
            {'name': 'Linux从入门到精通', 'price': '23.60', 'author': '一位不愿意透漏姓名的网友'},
            {'name': '鸟哥的Linux私房菜', 'price': '87.30', 'author': '一位不愿意透漏姓名的网友'},
            {'name': 'Python 3网络爬虫开发实战', 'price': '49.50', 'author': '一位不愿意透漏姓名的网友'},
            {'name': 'Java基础', 'price': '47.10', 'author': '一位不愿意透漏姓名的网友'},
            {'name': '世界上最好的语言-PHP', 'price': '12.30', 'author': '一位不愿意透漏姓名的网友'},
            {'name': 'Elasticsearch实战', 'price': '39.30', 'author': '一位不愿意透漏姓名的网友'},
            {'name': 'Redis设计与实现', 'price': '47.30', 'author': '一位不愿意透漏姓名的网友'}
        ]
        return goods_list


class Settlement:
    pass


def main():
    # 实例化用户
    name = '愿意透漏姓名的网友'
    user = User(name, 1)
    print('Hi ' + user.name + '! 欢迎来到996超市！')

    print('目前的商品列表如下：')
    # 创建商品列表
    goods = Goods()
    goods_list = goods.goods_list()

    for (key, good) in enumerate(goods_list):
        print(
            '商品编号：' + str(key) + '    商品名称：' + good['name'] +
            '    价格：' + good['price'] + '    作者：' + good['author'])

    while True:
        input_num = input('请输入商品编号购买商品：')
        if input_num == '':
            print('请输入商品编号购买商品！')
            continue

        goods_number = int(input_num)
        print(goods_number)

        if goods_number >= len(goods_list):
            print('商品不存在,请输入正确的商品编号...')
            continue
        user.buy(goods_list[goods_number])

        cart_list = user.cart_goods()
        print('当前您的购物车里有：')
        total = 0
        for good in cart_list:
            print(good)
            total += float(good['price'])
        user.cart_price = total
        print('商品共 %s 件，共计 ￥：%s元' % (len(cart_list), total))

        option = input('继续购买请回车，结算请输入：(ok)，退出系统请输入：(q) ')
        if option == 'ok':
            user.pay()
            print('结算完成，退出系统')
            exit()
        elif option == 'q':
            print('欢迎下次光临！')
            exit()
        else:
            pass


if __name__ == '__main__':
    main()
