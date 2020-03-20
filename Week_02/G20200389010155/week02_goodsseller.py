"""
为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：

普通用户消费不足 200 元，无折扣，原价付费；
普通用户消费满 200 元打九折；
VIP 会员满 200 元打八折；
VIP 会员满 10 件商品打八五折。
要求：
请使用面向对象编程实现结算功能。
由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。
"""
class discount(object):
    def __init__(self):
        self.price={'tomato': 5, 'shampoo': 68, 'milk': 36, 'potato': 6, 'noodle': 10, 'rice': 38, 'flour': 25, 'banana': 47,
             'orange': 35, 'coco': 3, 'cake': 20}

    def sellsum(self):
        print("please input your goods list")
        selllist = {}
        judgeflag = True
        while judgeflag:
            # 提示输入商品种类和数量
            goodslist = str(input('input goods type:'))
            qualitylist = int(input('input goods quality:'))
            selllist[goodslist] = qualitylist
            # 判断是否继续输入
            qa = input('是否继续购买?(yes/no)')
            if qa == 'no':
                judgeflag = False
        sum = 0
        goodsnum=0
        for k, v in selllist.items():
            sum = sum + int(self.price[k])*int(v)
            goodsnum =goodsnum+int(v)
        return sum,goodsnum

class vip(discount):
    def __init__(self):
        super().__init__()
    def vipdiscnt(self):
        ret,numcnt=self.sellsum()
        sumcnt1=ret*float(0.8) if ret >=200 else ret
        sumcnt2=ret*float(0.85) if numcnt >=10 else ret
        sumcnt = sumcnt1 if sumcnt1 < sumcnt2 else sumcnt2
        return sumcnt
class common(discount):
    def __init__(self):
        super().__init__()
    def commondiscnt(self):
        ret,_=self.sellsum()
        sumrst= ret*float(0.9) if ret >=200 else ret
        return sumrst

if __name__ == '__main__':
    userflag=input('input user flag(vip/common):')
    vipuser=vip()
    commonuser=common()
    totalsum= vipuser.vipdiscnt() if userflag=='vip' else commonuser.commondiscnt()
    print("您的购物清单结算费用为:%.2f"%totalsum)