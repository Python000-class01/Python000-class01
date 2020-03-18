
class Goods (object):

    def __init__(self,price):
        self.price = price


class Customer (object):

    def __init__(self,goods_list):
        self.goods_list = goods_list

    def pay (self):
        expend = 0
        for good in self.goods_list:
            expend += good.price

        return expend


class CommonCustomer (Customer):

    def pay (self):
        cost = super(CommonCustomer, self).pay()

        if cost >= 200:
            all_cost = cost*0.9
            return all_cost
        else:
            return cost


class VipCustormer (Customer):

     def pay (self):
        cost = super(VipCustormer, self).pay()
        if cost >= 200 and len(self.goods_list)>= 10:
            all_cost1 = cost*0.8
            all_cost2 = cost * 0.85
            return min(all_cost2, all_cost1)
        elif len(self.goods_list)>= 10:
            all_cost2 = cost*0.85
            return all_cost2
        elif cost >= 200 :
            all_cost1 = cost * 0.8
            return all_cost1
        else:
            return cost


def store_996():
    list_goods = [Goods(1), Goods(20), Goods(3), Goods(4), Goods(5),
                Goods(10), Goods(20), Goods(30), Goods(40), Goods(50)]

    common = CommonCustomer(list_goods)
    vip = VipCustormer(list_goods)

    total_pay = Customer(list_goods).pay()

    print("总费用：%.1f" % total_pay)
    print("普通会员支付：%.1f" % common.pay())
    print("VIP会员支付：%.1f" % vip.pay())


if __name__ == '__main__':
    store_996()