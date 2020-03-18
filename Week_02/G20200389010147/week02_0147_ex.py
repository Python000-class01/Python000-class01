# 父類別-用户
class Cust(object):
    def __init__(self,consumption, product_cnt, cust_lv):
        self.consumption = consumption
        self.product_cnt = product_cnt
        self.cust_lv = cust_lv

    def getConsumption(self):
        return self.consumption

# 子類別-普通用户
class normCust(Cust):
    def __init__(self, consumption, product_cnt, cust_lv='norm'):
        super().__init__(consumption, product_cnt, cust_lv)

    # 普通用户消费不足 200 元，无折扣，原价付费；普通用户消费满 200 元打九折；
    def getConsumption(self):
        if self.consumption < 200:
            return self.consumption
        elif self.consumption >= 200:
            return self.consumption*0.9

# 子類別-VIP 会员
class vipCust(Cust):
    def __init__(self, consumption, product_cnt, cust_lv='vip'):
        super().__init__(consumption, product_cnt, cust_lv)

    # VIP 会员满 200 元打八折；VIP 会员满 10 件商品打八五折。两种折扣方式，根据最优惠的价格进行结算。
    def getConsumption(self):
        if (self.consumption<200) & (self.product_cnt<10):
            return self.consumption
        elif (self.consumption<200) & (self.product_cnt>=10):
            return self.consumption*0.85
        else:
            return self.consumption*0.8

class Factory:
    def getTotalConsumption(self, consumption, product_cnt, cust_lv):
        if cust_lv == 'vip':
            return vipCust(consumption, product_cnt).getConsumption()
        elif cust_lv == 'normal':
            return normCust(consumption, product_cnt).getConsumption()

if __name__ == '__main__':
    factory = Factory()
    # vip會員價格
    vip_cust_consumption = factory.getTotalConsumption(200, 10, 'vip')
    # 普通用戶價格
    norm_cust_consumption = factory.getTotalConsumption(100, 5, 'normal')
    print('某vip會員花費: ', vip_cust_consumption)
    print('某普通用戶花費: ', norm_cust_consumption)