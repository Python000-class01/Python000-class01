#第一种原始程序,售货员手动输入商品价格和数量

class People():
    def __init__(self,name,vip=False):
        self.name = name
        self.vip =vip


    def buy(self):
        zongjia =  0
        allcount = 0
        while True:
            price = float(input('请输入商品的价格：'))
            count = float(input('请输入商品的数量：'))
            zongjia = zongjia+ price*count
            allcount =allcount + count
            #print("你购买了{}件商品，总价是{}元".format(allcount,zongjia))
            choice=input("继续添加请输入1，结算请输入2：")
            if choice == '2':
                if self.vip == False:
                    print('您是普通会员，考虑办卡么')
                    if zongjia < 200:
                        zongjia =zongjia
                    else:
                        zongjia = 0.9*zongjia
                    print("你购买了{}件商品，总价是{}元".format(allcount, zongjia))
                    print('欢迎下次光临')
                    break
                elif self.vip ==True:  #这里需要改一下因为85折肯定多于8折  改成75折比较好。
                    print('欢迎尊敬的VIP用户')
                    if zongjia > 200 and allcount > 10:
                        zongjia1 = 0.8 * zongjia
                        zongjia2 = 0.85*zongjia
                        if zongjia1 >zongjia2:
                            zongjia = zongjia2
                        else:
                            zongjia = zongjia1
                    elif zongjia > 200 and allcount < 10 :
                        zongjia = 0.8 * zongjia
                    elif  allcount > 10:
                        zongjia = 0.85*zongjia
                    else:
                        zongjia = zongjia
                    print("你购买了{}件商品，总价是{}元".format(allcount, zongjia))
                    print('欢迎下次光临')
                    break
                else:
                    pass
            else:
                continue




def main():
    name = '小红'
    vip = False
    print(name +'欢迎来到996超市！')
    print('我是收费员，接下去我帮你结算金额')
    a =People('小红')
    b = a.buy()



if __name__ == '__main__':
    main()


#优雅的方式，从菜单中自动售货
import pandas as pd
import numpy as np

list = pd.DataFrame(data=[['青菜', 10], ['白菜', 10], ['萝卜', 10], ['花菜', 10]], columns=['商品名', '价格'], index=[1, 2, 3, 4])
#偷懒了 可以定义一个类 方便增加减少

class Shop():
    def __init__(self, name):
        self.name = name

    def buy(self):
        self.price = 0
        self.allcount = 0
        while True:
            print("欢迎来到996超市,请选择你要购买的商品编号")
            print(list)
            num = int(input('请输入购买商品的编号：'))
            count = int(input('请输入购买商品的数量：'))
            self.price += list.iloc[num - 1, 1] * count
            self.allcount += count
            # print("你购买了{}件商品，总价是{}元".format(allcount,zongjia))
            choice = input("继续添加请输入1，结算请输入2：")
            if choice == '2':
                # print("你购买了{}件商品，总价是{}元".format(self.allcount,self.price))
                break
            else:
                continue


class Not_vip(Shop):
    def __init__(self, name):
        super(Shop, self).__init__()

    def pay(self):
        print('您是普通会员，考虑办卡么')
        if self.price < 200:
            price = self.price
        else:
            price = 0.9 * self.price
        print("你购买了{}件商品，总价是{}元".format(self.allcount, price))
        print('欢迎下次光临')


class Vip(Shop):
    def __init__(self, name):
        super(Shop, self).__init__()

    def pay(self):
        print('欢迎尊敬的VIP用户')
        if self.price > 200 and self.allcount > 10:
            zongjia1 = 0.8 * self.price
            zongjia2 = 0.85 * self.price
            if zongjia1 > zongjia2:
                zongjia = zongjia2
            else:
                zongjia = zongjia1
        elif self.price > 200 and self.allcount < 10:
            zongjia = 0.8 * self.price
        elif self.allcount > 10:
            zongjia = 0.85 * self.price
        else:
            zongjia = self.price
        print("你购买了{}件商品，总价是{}元".format(self.allcount, zongjia))
        print('欢迎下次光临')


def main(name):
    chooice = int(input('会员请输入1，不是会员请输入2：'))
    if chooice == 1:
        a = Vip(name)
        print(a.buy())
        print(a.pay())
    else:
        a = Not_vip(name)
        print(a.buy())
        print(a.pay())



if __name__ == '__main__':
    main('小方')


