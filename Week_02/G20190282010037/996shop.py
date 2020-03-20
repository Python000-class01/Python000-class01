class customer:
    def __init__(self,vip,quantity,amount):
        self.quantity = quantity
        self.amount = amount
        self.vip = False


class Discount():
    
    def discount(self,customer):
        dis=1
        if customer.vip:
            if customer.amount>200:
                dis= 0.8
            elif customer.quantity>10:
                dis=0.85
        else:
            dis= 0.9 if customer.amount>200 else 1

        return dis*customer.amount


if __name__ == '__main__':
    cus = customer
    cus.vip = int(input('请输入是否为VIP，1为是，0为否：'))
    cus.quantity = int(input('请输入所购数量：'))
    cus.amount = float(input('请输入所购总金额：'))
    paymoney = Discount().discount(cus)
    print("应付金额为："+str(paymoney))



        