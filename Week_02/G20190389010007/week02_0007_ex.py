from functools import reduce
price_dict = {"Pen":10,"Apple":10,"Face Mask":100,"Tea":30,"Milk":50}
goods_list = ["Pen","Apple","Face Mask","Tea","Milk"]

# 普通用户消费不足 200 元，无折扣，原价付费；
# 普通用户消费满 200 元打九折；
# VIP 会员满 200 元打八折；
# VIP 会员满 10 件商品打八五折。
class Custom(object):
    # 顾客
    def __init__(self, name, goods=None):
        goods=[]
        self.discount_rate = 0.9
        self.name = name
        self.goods = goods
        self.using_discount_rate =1
    
    def buy(self, goods_name):
        # 购买物品
        self.goods.append(goods_name)
    @property
    def total_price(self):
        return reduce(lambda a,b: a+b,[price_dict[i] for i in self.goods])
    def pay_up(self):
        # 结账
        if(self.total_price<200):
            self.final_prince = self.total_price
        else:
            self.final_prince = self.total_price * self.discount_rate
            self.using_discount_rate = self.discount_rate
        print(f'ok! this is ur bill')
        print(self.name)
        for item in self.goods:
            print(item)
        print(f'origin price is {self.total_price}')
        print(f'discount_rate is {self.using_discount_rate}')
        print(f'final price is {self.final_prince}')
class VIPCustom(Custom):    
    # VIP顾客
    def __init__(self, name, goods=None):
        super().__init__(name,goods=None),
        self.discount_rate = 0.8
        self.discount_num = 10
        self.discount_num_rate = 0.85
        self.using_discount_rate =1
    def pay_up(self):
        # 结账
        if(self.total_price<200 and len(self.goods)<10):
            self.final_prince = self.total_price
        elif(self.total_price<200 and len(self.goods)>=10):
            self.final_prince = self.total_price * self.discount_num_rate
            self.using_discount_rate=self.discount_num_rate
        elif(self.total_price>200):
            self.final_prince = self.total_price * self.discount_rate  
            self.using_discount_rate = self.discount_rate   
        print(f'ok! this is ur bill')
        print(self.name)
        for item in self.goods:
            print(item)
        print(f'origin price is {self.total_price}')
        print(f'discount_rate is {self.using_discount_rate}')
        print(f'final price is {self.final_prince}')

def input_goods_index():
    buyed_item = input(f'input the index of  what u want ')
    if int(buyed_item) not in list(range(len(goods_list))):
        print("wrong input ")
        return -1
    else:
        print("add item into cart ! ")
        return int(buyed_item)
if __name__=="__main__":
    print('==============================')
    print('welcome to 996_supermarket ')
    custom_name = input('input ur name \n')
    custom_type = input('r u vip of this supermarket? yes or no\n')
    custom = None
    if(custom_type =='yes'):
        print('u r our vip Welcome!')
        custom=VIPCustom(custom_name)
    else:
        print('Welcome!')
        custom=Custom(custom_name)
    print("buy something? ")
    [print(f'{index}. {g} ${price_dict[g]}') for index,g in enumerate(price_dict)]
    while True:
        re = input_goods_index()
        if(re>=0):
            custom.buy(goods_list[re])
            buy_re = input(f'do u wanna buy something more,y or n\n')
            if (buy_re !='y'):
                break
    custom.pay_up()
    print('bye!')

    



        

  
        

    
    




