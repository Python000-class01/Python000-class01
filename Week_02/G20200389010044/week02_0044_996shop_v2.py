# Author: Zts0hg
# Date: 2020-03-17 16:36:20
# LastEditTime: 2020-03-17 16:36:20
# LastEditors: Zts0hg
# Description: Win10, VSCode, python3.8.2
# FilePath: https://github.com/Zts0hg/Python000-class01/tree/master/Week_02/G20200389010044/week02_0044_996shop_v2.py
# TODO: 修改version1中商店进货和用户购买需要遍历字典依次调用purchase()和buy()函数的繁琐
import copy

class consumer(object):
    '''
    用户类
    属性:   姓名 - 标识用户
            角色 - 区分普通用户和VIP用户，按照不同结算规则结算
            购物车 - 储存用户当前购买行为所要购买的商品
    方法:   加入购物车 - 输入指定商品以及购买数量加入购物车
            移出购物车 - 输入指定商品以及要移出的数量
    '''
    # 如果把_cart 设置为静态字段，则每个实例的_cart共享同一块内存，即共用同一个购物车
    def __init__(self, name, role='ordinary'):
        self.name = name
        self._role = role
        self._cart = {}

    @property
    def cart(self):
        return self._cart

    @cart.deleter
    def cart(self):
        self._cart.clear()
    
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role
    
    def buy(self, *args, **kargs):
        # 传入商品清单 - 字典
        if len(args) == 1:
            for item in args[0]:
                if item not in self._cart:
                    self._cart[item] = args[0][item]
                else:
                    self._cart[item] += args[0][item]
        # 传入商品
        elif len(args) == 2:
            if args[0] not in self._cart:
                self._cart[args[0]] = args[1]
            else:
                self._cart[args[0]] += args[1]
        else:
            print("Something wrong in input.")

    def remove(self, *args, **kargs):
        '''
        从购物车中移除指定数量的指定商品
        如果指定数量少于购物车中指定商品存在的数量，则移除指定数量，并输出提示
        如果指定数量多于购物车中指定商品存在的数量，则移除该商品，并输出提示
        '''
        if len(args) == 1:
            for item in args[0]:
                if item not in self._cart:
                    print(f"remove 0 {args[0]} from {self.name}'s cart, now 0 {args[0]} exits.")
                else:
                    if args[0][item] < self._cart[item]:
                        self._cart[item] -= args[0][item]
                        print(f"remove {args[0][item]} {item} from {self.name}'s cart, now {self._cart[item]} {item} exits.")
                    else:
                        num = self._cart.pop(item)
                        print(f"remove {num} {args[0]} from {self.name}'s cart, now 0 {args[0]} exits.")
        elif len(args) == 2:
            if args[0] in self._cart:
                if args[1] < self._cart[args[0]]:
                    self._cart[args[0]] -= args[1]
                    print(f"remove {args[1]} {args[0]} from {self.name}'s cart, now {self._cart[args[0]]} {args[0]} exits.")
                else:
                    num = self._cart.pop(args[0])
                    print(f"remove {num} {args[0]} from {self.name}'s cart, now 0 {args[0]} exits.")

            elif args[0] not in self._cart:
                print(f"remove 0 {args[0]} from {self.name}'s cart, now 0 {args[0]} exits.")
        else:
            print("Something wrong in input.")

class shop(object):
    '''
    商品类
    属性：  货物 - 储存该商店销售的商品及对应价格
    方法:   进货 - 输入货物以及价格（成本价或零售价）
            结算 - 输入用户，商品，按照结算规则进行消费金额的计算
    '''
    def __init__(self, name):
        self.name = name
        self._goods = {}

    @property
    def goods(self):
        return self._goods
    
    def purchase(self, *args, **kargs):
        # 传入商品清单 - 字典
        if len(args) == 1:
            for item in args[0]:
                # 没有则视为进货，存在则视为更新价格
                self._goods[item] = args[0][item]

        # 传入商品
        elif len(args) == 2:
            self._goods[args[0]] = args[1]
        else:
            print("Something wrong in input.")
    
    def account(self, consumer):
        '''
        折扣都是在原价上进行，所以先算原价，再根据不同情况对金额运算
        '''
        total = 0   # 记录总消费金额
        count = 0   # 记录商品件数
        # 计算购物车商品总价
        for item in consumer.cart:
            count += consumer.cart[item]
            total += self._goods[item] * consumer.cart[item]
        # 普通用户计算优惠
        if consumer.role == "ordinary":
            if total >= 200:
                total *= 0.9
        
        # vip用户计算优惠
        elif consumer.role == "vip":
            # 满200元的折扣力度最大，所以最先计算该情况
            if total >= 200:
                total *= 0.8
            elif count >= 10:
                total *= 0.85
        # 打印票据
        print(f"996 Shop Receipt for {consumer.name}({consumer.role}):\nAmounts\tunit price\tItems\t")
        for item in consumer.cart:
            print(f"{consumer.cart[item]}\t{self._goods[item]}\t\t{item}")
        print(f"\nTotal: ${total}")
        # 结算完成，清空用户购物车
        del consumer.cart
        return total



if __name__ == '__main__':
    # 开一家名为996的商店
    Myshop = shop("996")

    # 给996商店进货
    goodsList = {
        "cola" : 3,
        "chips" : 5,
        "milktea" : 20,
        "coffee" : 20,
        "steak" : 50,
        "python" : 2000,
        "fox" : 2000
    }
    # for goods in goodsList:
    #     Myshop.purchase(goods, goodsList[goods])

    Myshop.purchase(goodsList)
    Myshop.purchase("lamp", 40)

    # 出现消费者
    andrew = consumer("andrew")
    anderson = consumer("anderson")
    ruo = consumer("ruo", "vip")

    # 消费者产生消费意向
    ruoList = {
        "cola" : 6,
        "chips" : 5
    }
    ruo.buy(ruoList)        # 往购物车里放一堆 - 传入字典
    ruo.buy("python", 2)    # 往购物车里放一样

    # 消费者在996商店进行购买并结算
    Myshop.account(ruo)
    print(f"After accountting, ruo's cart:\n{ruo.cart}")