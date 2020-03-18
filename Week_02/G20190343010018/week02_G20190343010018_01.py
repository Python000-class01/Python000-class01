def vip(amount, num):
    if amount >= 200:
        return amount * 0.8
    elif amount < 200 and num >= 10:
        return amount * 0.85
    else:
        return amount

def normal(amount):
    if amount >= 200:
        return amount * 0.9
    return amount

def pay(isvip,amount,num):
    if isvip == 1:
        return vip(amount,num)
    else:
        return normal(amount)

def isint(n):
    while True:
        try:
            n = int(n)
            break
        except:
            n = input("输入错误，只能为数字")
    return n

if __name__ == '__main__':
    isvip = input("输入是否为vip,1为vip，0为普通")
    isint(isvip)
    amount = input("输入金额")
    isint(amount)
    number = input("输入商品数量")
    isint(number)
    print(pay(int(isvip),int(amount),int(number)))