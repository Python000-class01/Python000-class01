class UserFactory(object):
    @staticmethod
    def get_user(name, user_type):
        if user_type == 'vip':
            return VipUser(name)
        if user_type == 'ordinary':
            return OrdinaryUser(name)
        return 'not a right user_type'


class User(object):
    def __init__(self, name):
        self.name = name


class OrdinaryUser(User):
    def __init__(self, name):
        super().__init__(name)

    def pay(self, price, num):
        total_cost = price * num
        if total_cost < 200:
            return total_cost
        if total_cost >= 200:
            return total_cost * 0.9


class VipUser(User):
    def __init__(self, name):
        super().__init__(name)

    def pay(self, price, num):
        total_cost = price * num
        if total_cost >= 200:
            return total_cost * 0.8
        if num >= 10:
            return total_cost * 0.85
        return total_cost


if __name__ == "__main__":
    ordinary_user = UserFactory.get_user('marry', 'ordinary')
    print('ordinary_user buy 200', ordinary_user.pay(200, 1))
    vip_user = UserFactory.get_user('katy', 'vip')
    print('vip_user buy num 10 cost 200', vip_user.pay(200, 10))
    print('vip_user buy cost 200', vip_user.pay(200, 1))
    print('vip_user buy 190', vip_user.pay(190, 1))
    print('vip_user buy num 10', vip_user.pay(10, 10))

