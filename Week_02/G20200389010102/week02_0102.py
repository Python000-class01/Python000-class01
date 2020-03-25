#goods_list = [['土豆',10],['番茄'],30]
class Customer(object):
    def __init__(self,goods_list):
        self.goods_list = goods_list

    def payMoney(self):
        total_money = 0
        #购买的商品总数
        total_goods = len(self.goods_list)
        if total_goods !=0:
            for goods in self.goods_list:
                total_money += goods[1]
        return total_money,total_goods


#普通顾客
class Shopper(Customer):
    def pay(self):
        total_money,total_goods = super().payMoney()
        if total_money >= 200:
            print(f'顾客您好，您总共消费{total_money}元，九折之后需要付费{total_money*0.9}元')
        else:
            print(f'顾客您好，您总共消费{total_money}元，需要付费{total_money}元')

#vip客户
class VipShopper(Customer):
    def pay(self):
        total_money, total_goods = super().payMoney()
        if total_money < 200 and total_goods < 10:
            print(f'尊敬的vip顾客您好，您总共消费{total_money}元，需要付费{total_money}元')
        elif total_money >= 200 and total_goods < 10:
            print(f'尊敬的vip顾客您好，您总共消费{total_money}元，需要付费{total_money*0.8}元')
        elif total_goods >= 10:
            if total_money < 200:
                print(f'尊敬的vip顾客您好，您总共消费{total_money}元，需要付费{total_money * 0.85}元')
            elif total_money >= 200:
                t_money1 = total_money * 0.85
                t_money2 = total_money * 0.8
                pay_money = lambda t_money1,t_money2 : t_money1 if t_money1 > t_money2 else t_money2
                tota_money = pay_money(t_money1,t_money2)
                print(f'尊敬的vip顾客您好，您总共消费{total_money}元,需要付费{tota_money}元')

class Factory(object):
    def payResult(self,vip,goods_list):
        if vip == 'vip':
            return VipShopper(goods_list).pay()
        elif vip == 'normal':
            return Shopper(goods_list).pay()
        else:
            pass

if __name__ == '__main__':
    goods_list = [['土豆', 10], ['番茄', 30],['番茄', 30],['番茄', 30],['番茄', 30],['土豆', 10],['番茄', 30],['土豆', 10],['番茄', 30],['土豆', 10],['番茄', 30],['番茄', 30]]
    factory = Factory()
    factory.payResult('vip',goods_list)