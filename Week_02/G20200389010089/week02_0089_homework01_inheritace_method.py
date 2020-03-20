####################################
#“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）
#的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：
#普通用户消费不足 200 元，无折扣，原价付费；
#普通用户消费满 200 元打九折；
#VIP 会员满 200 元打八折；
#VIP 会员满 10 件商品打八五折。
#要求：
#请使用面向对象编程实现结算功能。
#由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。
#---------------------------
# Use inheritance method
#
#################################
class Base(object):
    def __init__(self, name = None, membership = None, items = 0, orgcost = 0 ):
        self.name = name
        self.membership = membership
        self.items = items
        self.orgcost = orgcost
        self.discount = 0
        self.finalCost = 0

    def getName(self):
        return self.name

    def getMembership(self):
        return self.membership

    def getItems(self):
        return self.items

    def getOrgcost(self):
        return self.orgcost

    def getFinalCost(self):
        self.finalCost = self.orgcost *(1-self.discount)
        return self.finalCost

class Vip(Base):
    def __init__(self, name, membership,items, orgcost):
        super().__init__(name, membership,items, orgcost)
        print(f'Hi,Vip {name} , welcome to 996 Supermarket')
    
    def calculateDiscount(self):
        if self.orgcost >= 200:
            self.discount = 0.2
        elif self.items >= 10:
            self.discount = 0.15
        else:
            self.discount = 0


class Normal(Base):
    def __init__(self, name, membership,items, orgcost):
        super().__init__(name, membership,items, orgcost)
        print(f'Hi, member {name}, welcome to 996 Supermarket')
    
    def calculateDiscount(self):
            if self.orgcost >= 200:
                self.discount = 0.1
            else:
                self.discount = 0
class Factory:
    def getCustomer(self, name, membership,items, orgcost):
        if membership == 'Vip':
            return Vip(name, membership,items, orgcost)
        elif membership == 'Normal':
            return Normal(name, membership,items, orgcost)
        else:
            print(f'Hi, Please join the membership!')
            pass

if __name__ == '__main__':
    factory = Factory()
    #参数：姓名，会员属性，件数，总价
    customer = factory.getCustomer('Gao', 'Vip',10,250)
    customer.calculateDiscount()
    customer2 = factory.getCustomer('Zhang', 'Normal',10,250)
    customer2.calculateDiscount()
    customer3 = factory.getCustomer('Ni', 'Vip',10,180)
    customer3.calculateDiscount()
    customer4 = factory.getCustomer('Tang', 'Normal',13,190)
    customer4.calculateDiscount()
    print(f'---------------------------')
    print(f'Name : {customer.name} ')
    print(f'Mebership : {customer.membership} ')
    print(f'FinalCost :' ,customer.getFinalCost())
    print(f'---------------------------')
    print(f'Name : {customer2.name} ')
    print(f'Mebership : {customer2.membership} ')
    print(f'FinalCost :' ,customer2.getFinalCost())
    print(f'---------------------------')
    print(f'Name : {customer3.name} ')
    print(f'Mebership : {customer3.membership} ')
    print(f'FinalCost :' ,customer3.getFinalCost())
    print(f'---------------------------')
    print(f'Name : {customer4.name} ')
    print(f'Mebership : {customer4.membership} ')
    print(f'FinalCost :' ,customer4.getFinalCost())
    print(f'---------------------------')
