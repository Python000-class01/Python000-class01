class moneyspent(object):
    def __init__(self, vip=false, totalboughtquantity, moneytotalcost ):
        self.vip = vip
        self.totalboughtquantity = totalboughtquantity
        self.moneytotalcost = moneytotalcost


    def realcost(self,vip, totalboughtquantity, moneytotalcost):
        if self.vip:
            #
            if totalboughtquantity > 10:
                #
                if moneytotalcost > 200:
                    moneytotalcost = moneytotalcost * 0.8 * 0.85

            elif moneytotalcost > 200:
                finalrealcost = moneytotalcost * 0.8

            else:
                moneytotalcost = moneytotalcost

        elif moneytotalcost >= 200:
            finalrealcost = moneytotalcost * 0.9

        else:
            finalrealcost = moneytotalcost
        return finalrealcost


    def totalcost(self, quantity, price):
        moneytotalcost = quantity * price
        return moneytotalcost



   
