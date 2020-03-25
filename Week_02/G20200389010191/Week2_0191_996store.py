class Customer(object):
    def __init__(self, name, goods=None):
        self.name = name
        if goods is None:
            goods = {}
        self.goods = goods
        self.total = 0
    def buy(self, *args,**kwargs):
        # 购买物品
        self.goods = kwargs
        #print (self.goods)
    def discount(self):
        '''满200元打九折'''
        for value in self.goods.values():
            self.total = self.total + value
        if self.total > 200:
            self.total = 0.9*self.total
    
    def pay_up(self):
        # 结账
        print("Customer:"+self.name)
        print('Normal Custom')
        print("-"*30+"Receipt"+"-"*30)
        for key,value in self.goods.items():
            print(key+" "*10+str(value))
        print("Total： "+str(self.total))
    
        
class VipCustomer(Customer):
    def __init__(self,name):
        self.name = name
        self.total_dis1 = 0#第一类折扣算价
        self.total_dis2 = 0#第二类折扣算价
        self.discount_name =""#折扣名
        self.Original_price = 0#原价
    def Discount1(self):
        """满200打8折"""
        for value in self.goods.values():
            self.total_dis1 = self.total_dis1+value
        if self.total_dis1 > 200:
            self.total_dis1 = round(0.8 * self.total_dis1,2)
            #print("满200打8折："+str(self.total_dis1))
    def Discount2(self):
        """满10件打85折"""
        for value in self.goods.values():
            self.total_dis2 = self.total_dis2+value
        self.total_dis2 = round(0.85*self.total_dis2,2)
        #print("满10件打85折:"+str(self.total_dis2))
    def Compare(self):
        if len(self.goods.items())>=10:
            self.total = lambda x:self.total_dis2 if self.total_dis1>self.total_dis2 else self.total_dis1
            if self.total_dis1>self.total_dis2:
                self.total =self.total_dis2
                self.discount_name = "满10件打85折"
            else:
                self.total = self.total_dis1
                self.discount_name = "满200打8折"
        else:
            print("商品不足10件")
            self.total = self.total_dis1
            self.discount_name = "满200打8折"
    def payup(self):
        # 结账
        print("Customer:"+self.name)
        print('VIP Custom')
        print("-"*30+"Receipt"+"-"*30)
        for key,value in self.goods.items():
            print(key+" "*10+str(value))
            self.Original_price = self.Original_price+value
        print("Origin price：  "+str(self.Original_price))
        print("Discount Type：" + self.discount_name)
        print("Price after Discount： "+str(self.total))



if __name__ == '__main__':
    custom2 = Customer('Jerry')
    custom2.buy(cake=200.1, apple=24)
    custom2.discount()
    custom2.pay_up()
    print('='*100)
    vipcostom = VipCustomer("Tom")
    vipcostom.buy(a=280,b=1,c=2,d=4,e=5,f=3,g=2,h=1,t=1,o=2)
    vipcostom.Discount1()
    vipcostom.Discount2()
    vipcostom.Compare()
    vipcostom.payup()