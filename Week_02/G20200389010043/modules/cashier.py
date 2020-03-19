from modules.order import Order
from modules.promotion import Promotion
from modules.struct import User


class Cashier(object):

    def __init__(self, vipSystem, paymentSystem):  # 依赖注入
        self.vipSystem = vipSystem
        self.paymentSystem = paymentSystem

    def checkout(self, *items, user=None):
        if user is None:
            user = User()

        order = Order.createOrderFromItems(items)
        promotion = Promotion()
        activity = promotion.getApplicableActivity(user, order)
        order.applyPromotion(activity)
        return order

    def checkVIPCard(self, cardNumber):
        return self.vipSystem.validate(cardNumber)

    def pay(self, order, paidAmount):
        return self.paymentSystem.pay(order, paidAmount)
