from customer import Customer

#第三方支付平台
class ThirdPay(object):
    def __init__(self, name):
        self.name = name
    #第三方来完成交易
    def trade(self, customer, store, good, count):
        if store.hasTheGood(good):
            payMoney = good.price * count
            print(payMoney)
            if customer.type == 'normal':
                print('普通用户===')
                if(payMoney > 200):
                    payMoney = payMoney * 0.9
            elif customer.type == 'vip':
                print('VIP用户===')
                if(payMoney > 200):
                    payMoney = payMoney * 0.8
                if(count > 10):
                    payMoney = payMoney * 0.85
            customer.pay(payMoney)
            store.receive(payMoney)
