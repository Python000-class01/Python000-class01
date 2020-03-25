from store import MyGood, Store
from customer import Customer
from good import Good
from thirdpay import ThirdPay

#天猫超市
tMall = Store(10000)
#普通用户
Jack = Customer(1000, 'normal')
#VIP用户
Thomas = Customer(1000, 'vip')
#第三方支付平台
thirdPay = ThirdPay('支付宝')

#超市进货
tMall.stock(MyGood('大苹果', 10, 1))
tMall.stock(MyGood('橘子', 15, 2))
tMall.stock(MyGood('红苹果', 5, 1.5))
tMall.stock(MyGood('红苹果', 15, 1.5))

#交易、结账
thirdPay.trade(Jack, tMall, tMall.takeGoods('红苹果'), 11)
thirdPay.trade(Thomas, tMall, tMall.takeGoods('红苹果'), 11)

print(Jack.account, Thomas.account, tMall.account)



