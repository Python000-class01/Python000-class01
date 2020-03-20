##Python训练营第二周作业，纯新手在狂刷基础视频的情况下，写出这些，
##面向对象那个现在有一些感觉。
##本来想实现的是从两个列表里选择商品，然后用个计数器记录用户的购买次数，依次条件增加VIP购买
##还有个条件算购买的金额，到了200给提示是否增加购买等
##总之，想法是有的，感觉还差很多

food_list = [u'副食蔬菜类', u'1.牛奶', u'2.面包', u'3.香肠', u'4.饼干', u'5.果汁',
                u'6.大白菜', u'7.芹菜', u'8.洋葱', u'9.黄瓜', u'10.西红柿',
                    u'11.牛肉', u'12.羊肉', u'13.猪肉', u'14.鸡肉', u'15.草鱼']
food_price = [0, 21, 19, 36, 12, 16, 2, 3, 4, 2, 3, 38, 47, 40, 21, 35]

def Welcome(func):
    def nei(a, b):
        print('+++++++++++++++++++++')
        func(a, b)
        print('+++++++++++++++++++++')

    return nei

@Welcome 
def add(a, b):
    print(a + b)

c = 'Welcome '
d = 'to 996 e-shop'
print(add(c, d))

print(food_list[0:15])

while True:
    food_id = int(input('请选择您需要的商品号码：'))
      
    if food_id < len(food_list[0:15]):
            print('您选择的商品是 %s , 单价为 %s 元/克' %(food_list[food_id], food_price[food_id]))
    
    elif food_id > len(food_list[0:15]):
            print('您输入的商品序号不存在，请重新输入')
    

class User():
    def __init__(self, purchase, pay):
        self.purchase = purchase
        self.pay = pay


class Vip_user():
    def __init_(self, purchase_vip, pay_vip):
        self.purchase_vip = purchase_vip
        self.pay_vip = pay_vip



        

