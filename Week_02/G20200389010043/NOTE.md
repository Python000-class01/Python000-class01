学习笔记

A draft sequence diagram can be found [here](https://github.com/jiakai-li/Python000-class01/blob/master/Week_02/G20200389010043/geek-python-week2.jpeg?raw=true)

Module structure:
- Cashier：
  收银对象封装，主要的driver类，功能包括：结算(创建订单，获取优惠活动)，查看VIP卡是否有效，付款(通过PaymentSystem完成)
- Promotion:
  推广的封装，单例对象，考虑到每天996所以每次启动系统时获取一次当天有效的推广活动即可，
  主要功能包括：通过PromotionSystem获取当前有效的优惠活动，根据user, order判断最佳的推广活动
- Order:
  订单类的封装，主要功能包括：通过产品创建订单，添加删除订单中的产品，获取付款金额和优惠前金额
  用户通过create方法创建订单，\_\_init\_\_方法通过__create_key进行访问保护(后面可能要通过元类来处理创建时的行为)
- Struct: Item and User for simple structure
  用户和物品两个类相对比较简单，也没有什么方法，所以通过dataclass进行封装
- MockedSystem: PaymentSystem and VIPSystem for system mock
  因为这两个系统可能是单独的子系统，所以用户结算时通过这两个系统分别进行付款和VIP用户验证操作
