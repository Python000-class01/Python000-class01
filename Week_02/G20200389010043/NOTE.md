学习笔记

A sequence diagram draft can be found [here](https://github.com/jiakai-li/Python000-class01/blob/master/Week_02/G20200389010043/geek-python-week2.jpeg?raw=true)

Module structure:
- Cashier
- Promotion
- Order:
  订单类的封装，主要功能包括：通过产品创建订单，添加删除订单中的产品，获取付款金额和优惠前金额
  用户通过create方法创建订单，\_\_init\_\_方法需要
- Struct: Item and User for simple structure
  用户和物品两个类相对比较简单，也没有什么方法，所以通过dataclass进行封装
- MockedSystem: PaymentSystem and VIPSystem for system mock
  因为这两个系统可能是单独的子系统，所以用户结算时通过这两个系统分别进行付款和VIP用户验证操作
