class customer:
    def __init__(self,vip,quantity,amount):
        self.quantity = quantity
        self.amount = amount
        self.vip = False

from abc import ABC ,abstractmethod

class Promotion(ABC):
    @abstractmethod
    def discount(self,customer):
        pass

# 普通用户0.9折
class cusPromo(Promotion):
    def discount(self,customer):
        return 0.9 if customer.amount>200 else 1

# VIP用户0.8折
class vip1Promo(Promotion):
    def discount(self,customer):
        if(customer.vip):
            return 0.8 if customer.amount>200 else 1
        return 1

# VIP用户0.85折
class vip2Promo(Promotion):
    def discount(self,customer):
        if(customer.vip):
            return 0.85 if customer.quantity>10 else 1
        return 1
# 最优折扣计算
class BestDiscount(Promotion):
    def discount(self,customer):
        all_promotion=[globals()[name] for name in globals() if name.endswith('Promo')]
        return min([prom().discount(customer) for prom in all_promotion])*customer.amount


if __name__ == '__main__':
    cus = customer
    cus.vip = int(input('请输入是否为VIP，1为是，0为否：'))
    cus.quantity = int(input('请输入所购数量：'))
    cus.amount = float(input('请输入所购总金额：'))
    paymoney2=BestDiscount().discount(cus)
    print("应付最低金额为："+str(paymoney2))




        