from collections import ChainMap
import math
import random

class Product(object):
    def __init__(self):
        self.productDict = {}

    def addProduct(self,name,price):
        self.productDict[name] = price

    def addProdDict(self,pDict):
        self.productDict = dict(ChainMap(self.productDict,pDict))

    @property
    def getProdPrice(self,price):
        return self.productDict[name]
    
    @property
    def getProdDict(self):
        return self.productDict

class ShoppingCart(object):
    def __init__(self):
        self.cart = []
        self.cartCount = 0

    def addCart(self,product,name,count):
        self.cart.append([name,product[name],count])
    
    @property
    def deleteCart(self):
        self.cart = []
        self.cartCount = 0

    @property
    def getCartList(self):
        return self.cart

    @property
    def getCartCount(self):
        for i in self.cart:
            self.cartCount = self.cartCount + i[1]
        return self.cartCount


class Shelf(object):
    def __init__(self):
        self.shelfDict = {}
    
    def appendShelf(self,name,amount):
        self.shelfDict[name] = amount
    
    @property
    def getShelfList(self):
        return self.shelfDict

    @property
    def getCurrentProdNum(self,name):
        if self.shelfDict[name] == None:
            return 0
        return self.shelfDict[name]

    """
    获取所有商品
    """
    def getAllPrdct(self):
        pass

    def getAllCount(self):
        pass

class CustomerGen(ShoppingCart):
    def __init__(self,name):
        self.name = name
        self.vip = False
        super().__init__()
    
    def changeToVIP(self):
        self.vip = True
        return self.vip

    @property
    def amIVIP(self):
        return self.vip
    @property
    def getMyCart(self):
        return super().getCartList


class Discount(object):
    def __init__(self):
        self.pVIPDiscount = ()
        self.aVIPDiscount = ()
        self.normalDiscount = ()

    def setVIPPriDisc(self,totpri,discount):
        self.pVIPDiscount = (totpri,discount)

    def setVIPAmountDisc(self,amount,discount):
        self.aVIPDiscount = (amount,discount)
    
    def setNorDisc(self,totpri,discount):
        self.normalDiscount = (totpri,discount)
    
    @property
    def getVIPPriDisc(self):
        return self.pVIPDiscount

    @property
    def getVIPAmountDisc(self):
        return self.aVIPDiscount

    @property
    def getNorDiscount(self):
        return self.normalDiscount

class Settle(object):
    def __init__(self):
        self.noDiscSum = 0
        self.totalSum = 0
    
    def getNoDiscSum(self,cart):
        self.noDiscSum = 0
        for i in cart:
            self.noDiscSum = self.noDiscSum + i[1] * i[2]
        return self.noDiscSum

    def settlement(self,customer,discount):
        self.totalSum = 0
        self.customerName = customer.name
        if not customer.vip:
            if (n := self.getNoDiscSum(customer.getMyCart)) >= discount.getNorDiscount[0]:
                self.totalSum = n * discount.getNorDiscount[1]
            else:
                self.totalSum = n
        else:
            firstSum = 0
            secondSum = 0
            if (kk := self.getNoDiscSum(customer.getMyCart)) >= discount.getVIPPriDisc[0]:
                firstSum = kk * discount.getVIPPriDisc[1]
                if (c := customer.getCartCount) > discount.getVIPAmountDisc[0]:
                    secondSum = kk * discount.getVIPAmountDisc[1]
                    self.totalSum = min(firstSum,secondSum)
                else:
                    self.totalSum = firstSum
            else:
                firstSum = kk
                if (c := customer.getCartCount) > discount.getVIPAmountDisc[0]:
                    secondSum = kk * discount.getVIPAmountDisc[1]
                    self.totalSum = min(firstSum,secondSum)
                else:
                    self.totalSum = firstSum
        return self.totalSum


    

henry = CustomerGen("henry")
henry.changeToVIP()
mary = CustomerGen('mary')
prodList = Product()
prodList.addProduct("口罩",2)
prodList.addProduct("牙刷",4)
pDict = {'香烟':5,'纸巾':2,'可乐':5,'啤酒':30}
prodList.addProdDict(pDict)
shelf = Shelf()
discount = Discount()
discount.setVIPAmountDisc(10,0.85)
discount.setVIPPriDisc(200,0.8)
discount.setNorDisc(200,0.9)

for i in list(prodList.getProdDict):
    shelf.appendShelf(i,100)

shopCart = ShoppingCart()
for j in list(shelf.getShelfList):
    henry.addCart(prodList.getProdDict,j,random.randint(1,10))
    mary.addCart(prodList.getProdDict,j,random.randint(1,10))



settlement = Settle()

print(henry.name)
print('is vip :')
print(henry.vip)
print(henry.getMyCart)
print(settlement.settlement(henry,discount))
print(settlement.noDiscSum)

print(mary.name)
print('is vip :')
print(mary.vip)
print(mary.getMyCart)
print(settlement.settlement(mary,discount))
print(settlement.noDiscSum)