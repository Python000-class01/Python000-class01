from modules.promotion import *


class VIPSystem(object):
    # A mock for the VIP system

    VIPMembers = {'VIP001'}

    @classmethod
    def validate(cls, user):
        if user.VIPCardNum is not None:
            if user.VIPCardNum in cls.VIPMembers:
                return True
        return False


class PaymentSystem(object):
    # A mock for the payment system

    @classmethod
    def pay(cls, order, paidAmount):
        if order.amountDue > paidAmount:
            return -1
        return paidAmount - order.amountDue
