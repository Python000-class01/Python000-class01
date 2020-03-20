from week02_0076_commodity import Commodity
from week02_0076_customer import OrdinaryCtm,VIPCtm


def singleton(cls):
    instances={}
    def getinstance():
        if cls not in instances:
            instances[cls]=cls()
        return instances[cls]
    return getinstance

@singleton
class Store(object):
    def __init__(self):
        #便利店商品列表
        self._commodities_list={}
        #便利店进货
        self._produceCommodities()

    def custom_access(self):
        self.welcomeComing()
        self._showCommoditiesList()

    def welcomeComing(self):
        print('------------------996便利店，欢迎您的到来！---------------------\n')

    def _showCommoditiesList(self):
        print('----本店有商品如下：----')
        print('---商品名称    商品价格---')

        count = 1
        for commodity_name,commodity_price in self._commodities_list.items():
            print(f'{count}. {commodity_name}      {commodity_price}')
            count+=1
        print()

    def ctm_shopping(self,shoppingcar_list):
        while True:
            item=input('请输入您要购买的商品序号。如输入 可乐 代表可乐，输入 # 表示购买完毕，进行结算：\n')
            if item=='#':
                print()
                self._showCustomerList(shoppingcar_list)
                return shoppingcar_list
            if item not in self._commodities_list:
                print('本店暂无此商品，我们将努力购进您的需求！\n')
                continue
            number=input('请输入您要购买的数量，如输入 5 代表5份：\n')
            shoppingcar_list[item]+=int(number)
            print('添加购物车成功！\n')

    def _showCustomerList(self,shoppingcar_list):
        print('----您的购物车有如下商品：----')
        print('商品名称    商品数量')

        count = 1
        for commodity_name, commodity_number in shoppingcar_list.items():
            print(f'{count}. {commodity_name}  {commodity_number}')
            count += 1
            print()
            
        while True:
            state=input('输入 0 继续购物，输入 1 表示确认：\n')
            print()
            if state=='0':
                self.ctm_shopping(shoppingcar_list)
                return shoppingcar_list
            elif state=='1':
                return shoppingcar_list
            else:
                print('----小店不明白您在说什么---- \n')
                continue

    def cmt_calculatePrice(self,status,shoppingcar_list):
        total_money=0
        total_number=0

        for commodity_name, commodity_number in shoppingcar_list.items():
            single_price=self._commodities_list[commodity_name]
            total_money+=single_price*commodity_number
            total_number+=commodity_number

        if status==1 and total_money<200 and total_number<10 or status==0 and total_money<200:
            print(f'您需付{total_money}元')
        elif total_money>=200:
            if status==0:
                print(f'原价为{total_money}元，亲爱的用户已为您选择最优折扣，您需付{total_money*0.9}')
            else:
                print(f'原价为{total_money}元，尊敬的会员已为您选择最优折扣，您需付{total_money * 0.8}')
        elif status==1 and total_money<200 and total_number>=10:
            print(f'原价为{total_money}元，尊敬的会员已为您选择最优折扣，您需付{total_money * 0.85}')

        print('支付成功！\n')
        print('------------------996便利店，谢谢您的到来，期待您的下次光临！---------------------')

    def _produceCommodities(self):
        for Commdity in Commodity.__subclasses__():
            commodity=Commdity()
            self._commodities_list[commodity.name]=commodity.price



if __name__ == '__main__':
    store=Store()
    xiaoming=OrdinaryCtm('小明普通')
    xiaoming.accessStore(store)
    # xiaohua=VIPCtm('小华会员')
    # xiaohua.accessStore(store)