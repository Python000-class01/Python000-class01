class User(object):

    __slots__ = ['user_type', 'total_expense', 'total_number']

    def __init__(self, user_type, total_expense, total_number):
        self.user_type = user_type
        self.total_expense = total_expense
        self.total_number = total_number

    # 打印用户及消费信息
    def print_order_info(self, discount):
        final_expense = self.total_expense * discount
        print('The user type is {}, total expense is {}, discount is {}, final expense is {}'.
              format(self.user_type, self.total_expense, discount, final_expense))

    # 最优折扣
    def settle(self):
        # 默认折扣为1
        discount = 1
        if self.user_type == 'normal':
            if self.total_expense >= 200:
                discount = 0.9
        elif self.user_type == 'vip':
            if self.total_expense >= 200:
                discount = 0.8
            elif self.total_expense < 200 and self.total_number >= 10:
                discount = 0.85
        return self.print_order_info(discount)


user_01 = User('normal', 199, 9)
user_02 = User('normal', 200, 9)
user_03 = User('normal', 200, 10)
user_04 = User('vip', 199, 9)
user_05 = User('vip', 200, 9)
user_06 = User('vip', 200, 10)
user_07 = User('vip', 199, 10)
# user_08 = User('error_user_type', 199, 9)
user_01.settle()
user_02.settle()
user_03.settle()
user_04.settle()
user_05.settle()
user_06.settle()
user_07.settle()
# user_08.settle()

"""
The user type is normal, total expense is 199, discount is 1, final expense is 199
The user type is normal, total expense is 200, discount is 0.9, final expense is 180.0
The user type is normal, total expense is 200, discount is 0.9, final expense is 180.0
The user type is vip, total expense is 199, discount is 1, final expense is 199
The user type is vip, total expense is 200, discount is 0.8, final expense is 160.0
The user type is vip, total expense is 200, discount is 0.8, final expense is 160.0
The user type is vip, total expense is 199, discount is 0.85, final expense is 169.15
"""