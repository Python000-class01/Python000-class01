# 为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：

#     普通用户消费不足 200 元，无折扣，原价付费；
#     普通用户消费满 200 元打九折；
#     VIP 会员满 200 元打八折；
#     VIP 会员满 10 件商品打八五折。
#     要求：
#     请使用面向对象编程实现结算功能。
#     由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。

# 思路:使用工厂模式,先判断用户身份,然后进行结账运算
class Consumer(object):
    # 消费者:姓名,金额,件数,结算方式
    def __init__(self):             # 直接复制的话,会导致不同数据覆盖,
        self.name = None            # 这样,创建对象先赋值为0,然后再赋值.
        self.num = None
        self.vip = None
        self.cost = None
    def getName(self):
        return self.name
    def getNum(self):
        return self.num
    def getVip(self):
        return self.vip
    def getCost(self):
        return self.cost

class VipConsumer(Consumer):
    def __init__(self,name,cost,num):
        global money1,money2
        if cost > 200:
            money1 =  cost * 0.8
        if num >= 10:
            money2 = cost * 0.85
        if cost < 200 and num < 10:
            money = cost
        # 判断vip用户两种结算方式哪一种更优惠
        else:
            money = money2 if money1>money2 else money1
        print(f'{name} cost {money} yuan')
        

class NotVipConsumer(Consumer):
    def __init__(self,name,cost,num):
        money = cost*0.9 if cost>200 else cost
        print(f'{name} cost {money} yuan')

class Account:
    def getCount(self,name,num,vip,cost):
        if vip == "T":
            return VipConsumer(name,cost,num)
        if vip == "F":
            return NotVipConsumer(name,cost,num)

if __name__ == "__main__":
    account = Account()
    cost1 = account.getCount("Jack",11,"F",256)
    cost2 = account.getCount("Cook",11,"T",256)
    cost3 = account.getCount("Victoria",11,"T",196)
    cost4 = account.getCount("Jobs",9,"F",256)
    cost4 = account.getCount("Robin",11,"F",196)
    