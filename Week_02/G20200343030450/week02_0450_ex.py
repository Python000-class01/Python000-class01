class Discount_996_Store:

    def __init__(self, isVIP=False, goods_num=0, total_price=0.0):

        self.isVIP = isVIP

        self.goods_num = goods_num

        self.total_price = total_price



    def Payformoney(self,isVIP,goods_num, total_price):

        out = total_price;

        if isVIP == TRUE:

            if total_price >=200:

                out = total_price * 0.8

            elif num >= 10:

                out = total_price * 0.85

        else:

            if total_price>=200:

                out = total_price * 0.9

        return out