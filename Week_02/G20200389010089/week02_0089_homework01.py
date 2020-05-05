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
#################################
class Base(object):
    def __init__(self, name, count = 0, orgCost = 0):
        self._type = None
        self.name = name
        self.count = count
        self.cost = orgCost
        self.discount = 0
        self.finalCost = 0
        
        @property
        def customerType(self):
            print(self._type)

        @customerType.setter
        def customerType(self, value):
            self._type = value

        @customerType.deleter
        def customerType(self):
            del self._type

    def counting(self):
        if self.type == 'vip':
            if self.cost >= 200:
                self.discount = 0.2
            elif self.count >= 10:
                self.discount = 0.15
            else:
                self.discount = 0
        else:
            if self.cost >= 200:
                self.discount = 0.1
            else:
                self.discount = 0
        
        self.finalCost = self.cost*(1-self.discount)

if __name__ == '__main__':
    m1 = Base('gao',10,250)
    m1.type = 'normal' 

    m2 = Base('zhang',10,250)
    m2.type= 'vip'

    m1.counting()
    m2.counting()
    print('--------------------------')
    print(str(m1.name),'is', str(m1.type),'member.' )
    print('Discount :',str(m1.discount*100),'%')
    print('Final Cost :',m1.finalCost)
    print('--------------------------')
    print(m2.name,'is', str(m2.type),'member.' )
    print('Discount :',str(m2.discount*100),'%')
    print('Final Cost :',m2.finalCost)


