class Cus_N(object):
    def Invoicy(self):
        Zu = self.Picky()
        print('-------------------------------------------------------')
        S_price = int(Zu)
        if S_price >= 200:
            Price = S_price * 0.9
        else:
            Price = S_price
        print('You need to pay $'+str(Price))
        return Price 
    def Picky(self):
        D_name = {
            1:"肥宅快乐水",
            2:"薯片",
            3:"寿司",
            4:"泡面",
            5:"火龙果",
            6:"榴莲",
            7:"关东煮",
            8:"てんぷら",
            9:"白い恋人"
            }
        D_price ={
            "肥宅快乐水":"7",
            "薯片":"18",
            "寿司":"28",
            "泡面":"10",
            "火龙果":"25",
            "榴莲":"180",
            "关东煮":"35",
            "てんぷら":"40",
            "白い恋人":"66"
            }
        print('Please look at this list')
        for x in range(1,len(D_name)+1):
            print(x,D_name[x],D_price[D_name[x]])
        Ans = ''
        Z_price = 0
        while Ans != 'n':
            Codey = int(input("Please input the Commodity's Coding"))
            Numbery = int(input('How many do you want?'))
            x = int(D_price[D_name[Codey]])
            y = Numbery
            d_price = x * y
            Z_price = Z_price + d_price
            Ans = input('Calculate the price(n)/keep buying(Anykeys but n)')
        return Z_price
def desc(res_func):
    def wrapper(self,*args,**kwargs):
        res = res_func(self,*args,**kwargs)
        if res[0] < 200 and res[1]>= 10:
            print('You bought '+str(res[1])+' items')
            print('You need to pay $'+str(res[0] * 0.85))
    return wrapper
class Cus_V(Cus_N):
    @desc
    def Invoicy(self):
        Tup = self.Picky()
        print('-------------------------------------------------------')
        Num = Tup[1]
        S_price = Tup[0]
        if S_price >= 200:
            Price = S_price * 0.8
            print('You bought '+str(Num)+' items')
            print('You need to pay $'+str(Price))
        elif S_price < 200 and Num>=10:
            Price = S_price
        else:
            Price = S_price
            print('You bought '+str(Num)+' items')
            print('You need to pay $'+str(Price))
        return Price,Num 
    def Picky(self):
        D_name = {
            1:"肥宅快乐水",
            2:"薯片",
            3:"寿司",
            4:"泡面",
            5:"火龙果",
            6:"榴莲",
            7:"关东煮",
            8:"てんぷら",
            9:"白い恋人"
            }
        D_price ={
            "肥宅快乐水":"7",
            "薯片":"18",
            "寿司":"28",
            "泡面":"10",
            "火龙果":"25",
            "榴莲":"180",
            "关东煮":"35",
            "てんぷら":"40",
            "白い恋人":"66"
            }
        print('Please look at this list')
        for x in range(1,len(D_name)+1):
            print(x,D_name[x],D_price[D_name[x]])
        Ans = ''
        Z_price = 0
        self.Numbery = 0
        while Ans != 'n':
            Codey = int(input("Please input the Commodity's Coding"))
            Numb = int(input('How many do you want?'))
            x = int(D_price[D_name[Codey]])
            y = Numb
            d_price = x * y
            self.Numbery = self.Numbery + y
            print(self.Numbery)
            Z_price = Z_price + d_price
            print(Z_price)
            Ans = input('Calculate the price(n)/keep buying(Anykeys but n)')
        return Z_price,self.Numbery
def main():
    print('Welcome to 996 store!!!')
    Answer = input('Are you a menber? y/n')
    if Answer =='y':
        Your_list = Cus_V()
        Your_list.Invoicy()
    else:
        Your_list = Cus_N()
        Your_list.Invoicy()
main()