# =====================================
# 第二周作业
# 为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：
# 普通用户消费不足 200 元，无折扣，原价付费；
# 普通用户消费满 200 元打九折；
# VIP 会员满 200 元打八折；
# VIP 会员满 10 件商品打八五折
# =====================================

# 定义普通顾客类
class Person(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


# 定义VIP普通顾客类
class VipPerson(Person):
    pass


# 定义售价函数
def Sale(Person, money: float, count: int):
    name = Person.__class__.__name__
    if (name == 'Person'):
        if(money < 200):
            return money
        else:
            return money*0.9
    elif (name == 'VipPerson'):
        if (money < 200 and count < 10):
            return money
        elif (money < 200 and count >= 10):
            return money*0.85
        else:
            return money*0.8


# 测试函数
if __name__ == "__main__":
    Tom = Person('Tom')
    Jerry = VipPerson('Jerry')
    print(Sale(Tom, 200, 10))
    print(Sale(Jerry, 150, 10))
