class Shop():
    def Checkout(self, Customer):

        total = Customer.GetTotal()
        number = Customer.GetNumber()
        str1="no off"
        if Customer.mold == 'normal':
            if total > 200:
                total = total * 0.9
                str1="9 off"
        elif Customer.mold == 'vip':
            if total >= 200 :
                total = total * 0.8
                str1="8 off"
            elif number >= 10:
                total = total * 0.85
                str1="8.5 off"
        else:
            pass
        print('The Customer is ' + Customer.mold)
        print('takeoff is '+ str1)
        print('The bill is %.2f' % total)
        

class Customer():
    def __init__(self, mold):
        self.mold = mold
        self.bag = []
        self.total = 0
    def buy(self,goods):
        self.bag.append(goods)
        self.total += goods.GetPrice()    
    def GetTotal(self):
        return self.total
    def GetNumber(self):
        return self.bag.__len__()


class Goods():
    def __init__(self, name, price ):
        self.name = name
        self.price = price
    def GetPrice(self):
        return self.price

Cus = Customer('vip')   
a = Goods('a',10)
b = Goods('b',12)
c = Goods('c',13)
d = Goods('d',10)
e = Goods('e',100)
f = Goods('f',10)
g = Goods('g',10)
h = Goods('h',16)
i = Goods('i',10)
j = Goods('j',10)
k = Goods('k',11)
Cus.buy(a)
Cus.buy(b)
Cus.buy(c)
Cus.buy(d)
Cus.buy(e)
Cus.buy(f)
Cus.buy(g)
Cus.buy(h)
Cus.buy(i)
Cus.buy(j)
Cus.buy(k)
supermarket = Shop()
supermarket.Checkout(Cus)