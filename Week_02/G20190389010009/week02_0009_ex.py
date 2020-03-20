class Customer:
    """消费者总类"""

    def __init__(self, merchandise_nums, merchandise_cost):
        """

        :param merchandise_nums: 购买的商品数量
        :param merchandise_cost: 总共花的钱，单位元
        """
        self.merchandise_nums = merchandise_nums
        self.merchandise_cost = merchandise_cost

    def buy(self):
        """

        :return: 返回消费者的购买信息
        """

        print("消费者总共购买了%s个商品，总共花费了%s元。" % (self.merchandise_nums, self.merchandise_cost))


class NonVipCustomer(Customer):
    """普通消费者，继承消费者总类"""

    def __init__(self, merchandise_nums, merchandise_cost):
        super().__init__(merchandise_nums, merchandise_cost)

    def buy(self):
        """

        :return: 打印普通消费者的购买信息
        """
        if self.merchandise_cost >= 200:
            self.merchandise_cost *= 0.9

        super().buy()


class VipCustomer(Customer):
    """VIP消费者，继承消费者总类"""

    def __init__(self, merchandise_nums, merchandise_cost):
        super().__init__(merchandise_nums, merchandise_cost)

    def buy(self):
        """

        :return: 打印VIP消费者的购买信息
        """
        if self.merchandise_cost >= 200:
            self.merchandise_cost *= 0.8
        elif self.merchandise_nums >= 10:
            self.merchandise_cost *= 0.85

        super().buy()


###### test ######
# 非VIP顾客，未花到200
c_non_vip_below_200 = NonVipCustomer(10, 100)
c_non_vip_below_200.buy()

# 非VIP顾客，花到200
c_non_vip_over_200 = NonVipCustomer(10, 300)
c_non_vip_over_200.buy()

# VIP顾客，未花到200，未超过10件
c_vip_below_200_less_10 = VipCustomer(1, 100)
c_vip_below_200_less_10.buy()

# VIP顾客，未花到200，超过10件
c_vip_below_200_more_10 = VipCustomer(12, 100)
c_vip_below_200_more_10.buy()

# VIP顾客，花到200，未超过10件
c_vip_over_200_less_10 = VipCustomer(8, 300)
c_vip_over_200_less_10.buy()

# VIP顾客，花到200，超过10件
c_vip_over_200_over_10 = VipCustomer(20, 300)
c_vip_over_200_over_10.buy()
