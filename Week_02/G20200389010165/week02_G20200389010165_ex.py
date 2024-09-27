
class Order(object):
    def __init__(self,Member):
        self.Member = Member
        
    def getOrderPrice(self): 
        vip = self.Member.get_vip()
        price = 0 
        productNum = 0 
        productList =  self.Member.get_car().get_list
        for product in productList: 
            productname = list(product.keys())
            productname.remove("num")
            print(productname[0])                   
            price += product.get(productname[0]).getPrice()*product.get("num")
            productNum += product.get("num")
        if not vip:                     
            if  price < 200:
                return  price
            else:
                return  price*0.95 
        elif vip:
            if(productNum > 9 and price < 200):
                return price*0.85
            elif(price >= 200):
                return price*0.8 
            else:
                return price    
                
                        

class Member(object):
    def __init__(self,name,Car):
        self.__name = name
        self.__vip = False
        self.__car = Car
       
    def setVip(self,isOrNot): 
        self.__vip = isOrNot
        
    def get_vip(self):
        return self.__vip
    
    def get_car(self):
        return  self.__car   
     
   
          

class Product(object):
    def __init__(self,name,price,desc):
        self.name = name
        self.price = price
        self.desc = desc
        
    def getName(self):
        return  self.name  
    
    def getPrice(self):
        return self.price
    
    def getDesc(self):
        return self.desc
    
class Car(object):
    def __init__(self,list):
        self.__list = list 
        
    @property    
    def get_list(self):
        return self.__list    
        
    def addProduct(self,Product,num):
        self.__list.append({Product.getName():Product,"num":num})  
        
    def removeProduct(self,Product):
        for product in self.__list:
            if(product.get(Product.getName()) != None):
                self.__list.remove(product)    
                
product1 =  Product("铅笔",2.49,"自动铅笔")  
product2 =  Product("钢笔",240.50,"LV牌钢笔")
productList =[]
car = Car(productList)
car.addProduct(product1,3)
car.addProduct(product2,1)

member = Member("xidada",car)
member.setVip(False)
order = Order(member)
print(order.getOrderPrice())

                   
