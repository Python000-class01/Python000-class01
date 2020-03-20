from abc import ABC, abstractmethod

from modules.mocked_systems import VIPSystem


def singleton(myClass):
    instance = {}

    def getInstance(*args, **kwargs):
        if myClass not in instance:
            instance[myClass] = myClass(*args, *kwargs)
        return instance[myClass]

    return getInstance


@singleton
class Promotion(object):
    def __init__(self):
        self.activities = PromotionSystem.getCurrentActivities()

    def addActivity(self, activity):
        self.activities.add(activity)

    def getApplicableActivity(self, user, order):
        if len(self.activities) == 0:
            return 1
        activityApplied = None
        discountRate = 1
        for activity in self.activities:
            if activity.isApplicable(user, order) and activity.discountRate < discountRate:
                discountRate = activity.discountRate
                activityApplied = activity
        return activityApplied


class Activity(ABC):

    def __init__(self, activitiID, activityName, discountRate):
        self.activityName = activityName
        self.activitiID = activitiID
        self.discountRate = discountRate

    @property
    def discountRate(self):
        return self.__discountRate

    @discountRate.setter
    def discountRate(self, val):
        self.__discountRate = val

    @abstractmethod
    def isApplicable(self, user=None, order=None):
        pass

    def __str__(self):
        string = f"Activity: {self.activityName}, ID: {self.activitiID}, Discount rate: {self.discountRate}"
        return string


@singleton
class DefaultActivity(Activity):
    def __init__(self):
        super().__init__(activitiID='default', activityName='default', discountRate=1)

    def isApplicable(self, user=None, order=None):
        return True


@singleton
class Regular200Activity(Activity):
    def __init__(self):
        super().__init__(activitiID='regular200', activityName='regular200', discountRate=0.9)

    def isApplicable(self, user=None, order=None):
        if order is not None and order.amountDueBeforeDiscount >= 200:
            return True
        return False


@singleton
class VIP200Activity(Activity):
    def __init__(self):
        super().__init__(activitiID='vip200', activityName='vip200', discountRate=0.8)

    def isApplicable(self, user=None, order=None):
        if order is not None:
            if order.amountDueBeforeDiscount >= 200:
                if VIPSystem.validate(user):
                    return True
        return False


@singleton
class VIP10Activity(Activity):
    def __init__(self):
        super().__init__(activitiID='vip10', activityName='vip10', discountRate=0.85)

    def isApplicable(self, user=None, order=None):
        if order is not None:
            if order.totalItems >= 10:
                if VIPSystem.validate(user):
                    return True
        return False


class PromotionSystem(object):
    # A mock for the promotion system

    @classmethod
    def getCurrentActivities(cls):
        defaultActivity = DefaultActivity()
        regularActivity = Regular200Activity()
        vip10Activity = VIP10Activity()
        vip200Activity = VIP200Activity()
        return {defaultActivity, regularActivity, vip10Activity, vip200Activity}
