class Shop(object):
    name=None
    status=None
    # self.kind=None
    money=None
    kind=None
    def getNanme(self):
        return self.name
    def getStatus(self):
        return self.status
    def getMoney(self):
        return self.money
class Consumer(Shop):
    def __init__(self,name):
        self.name=name
        # self.status=status
     # @property
    def account(self,money):
        if money >=200:
            return 0.95*money
        else:
            return money
class Vip_Consumer(Shop):
    def __init__(self,name):
        self.name = name
        # self.status = status
    # @property
    def account(self,money,kind):
        if money < 200 and  kind <10:
            return 0.8*money
        elif money < 200 and kind >= 10:
            return 0.85*money
        else:
            return 0.8*money
#         装饰器修饰
def outer(func):
    def inner(*args,**kwargs):
        pass
    return inner


class Factory:
    def getPerson(self,name,status,money,kind):
        if status ==0:
            return Consumer(name).account(money)
        else:
            return Vip_Consumer(name).account(money,kind)
if __name__ =='__main__':
    factory=Factory()
    deco=Factory().getPerson('shuai',0,100,9)
    print(deco)
    vip=Factory().getPerson('shuai', 1, 188, 12)
    print(vip)





