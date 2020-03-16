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
'''import pands as  pd

class Food():
    def Food_list(self):
        Food_list =pd.DataFrom [
            {'name': '青菜', 'price': '10'},
            {'name': '白菜', 'price': '10'},
            {'name': '萝卜', 'price': '10'},
            {'name': '地瓜', 'price': '10'},
            {'name': '番茄', 'price': '10'}
        ]
        return Food_list



class Shop():
    def __init__(self, name,vip=False):
        self.name = name
        self.vip = vip
        self.allcount = 0
        self.zongjia = 0
        


    def pay(self):
        if self.vip == False:
            print('您是普通会员，考虑办卡么')
            if zongjia < 200:
                zongjia = zongjia
            else:
                zongjia = 0.9 * zongjia
            elif self.vip == True:  # 这里需要改一下因为85折肯定多于8折  改成75折比较好。
                print('欢迎尊敬的VIP用户')
                if zongjia > 200 and allcount > 10:
                    zongjia1 = 0.8 * zongjia
                    zongjia2 = 0.85 * zongjia
                    if zongjia1 > zongjia2:
                        zongjia = zongjia2
                    else:
                        zongjia = zongjia1
                elif zongjia > 200 and allcount < 10:
                    zongjia = 0.8 * zongjia
                elif allcount > 10:
                    zongjia = 0.85 * zongjia
                else:
                    zongjia = zongjia
                print("你购买了{}件商品，总价是{}元".format(allcount, zongjia))
                print('欢迎下次光临')
                else:
                    pass





def main():
    name = '小红'
    print('欢迎来到996超市！')
    print('选择你需要购买的蔬菜：')
    foods = Food()
    foods_list = foods.Food_list()
    for k,v in foods_list:
   


if __name__ == '__main__':
    main()'''


