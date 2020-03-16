import random


class Order(object):
    totalOrdersGenerated = 0
    orders = {}
    __create_key = "create_password"

    def __init__(self, create_key=None):
        assert (create_key and create_key == Order.__create_key), \
            "You need to guess the create key first"
        self.orderID = None
        self.items = []
        self.totalItems = 0
        self.amountDueBeforeDiscount = 0
        self.promotionApplied = None

    @staticmethod
    def generateRandomOrderID(dlength):
        return ''.join(random.choice('0123456789') for i in range(dlength))

    @classmethod
    def createOrderFromItem(cls, item):
        order = Order("create_password")
        orderID = Order.generateRandomOrderID(10)
        while (orderID in Order.orders):
            orderID = Order.generateRandomOrderID(10)

        order._addItem(item)
        order.orderID = orderID

        cls.orders.update({orderID: order})
        cls.totalOrdersGenerated += 1

        return order

    @classmethod
    def createOrderFromItems(cls, items):
        order = Order("create_password")
        orderID = Order.generateRandomOrderID(10)
        while (orderID in Order.orders):
            orderID = Order.generateRandomOrderID(10)

        order.orderID = orderID
        for item in items:
            order._addItem(item)

        cls.orders.update({orderID: order})
        cls.totalOrdersGenerated += 1

        return order

    @property
    def amountDue(self):
        discountRate = 1
        if self.promotionApplied:
            discountRate = self.promotionApplied.discountRate
        return discountRate * self.amountDueBeforeDiscount

    def addItem(self, item):
        self._addItem(item)
        Order.orders.update({self.orderID: self})

    def addItems(self, items):
        for item in items:
            self._addItem(item)
        Order.orders.update({self.orderID: self})

    def applyPromotion(self, activity):
        self.promotionApplied = activity

    def _addItem(self, item):
        self.items.append(item)
        self.amountDueBeforeDiscount += item.itemPrice * item.itemUnits
        self.totalItems += item.itemUnits

    def __str__(self):
        string = f"OrderID: {self.orderID}\nTotal Items: {self.totalItems}\nTotal Amount: {self.amountDueBeforeDiscount}"
        return string
