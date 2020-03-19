

def decorator(aclass):
    class User(object):
        def __init__(self, consum, nums, type):
            self.consum = consum
            self.nums = nums
            self.type = type

        def panduan(self):
            if self.type == 0:
                self.putong(self.consum)
            elif self.type == 1:
                self.vip(self.consum, self.nums)

        def putong(self, consum):
            aclass.putong(consum)

        def vip(self, consum, nums):
            print()
    return User

@decorator
class Settle(object):
    def __init__(self, type, consum, nums):
        self.type = type
        self.consum = consum
        self.nums = nums

    def panduan(self):
        if self.type == 0:
            self.putong(self.consum)
        elif self.type == 1:
            self.vip(self.consum, self.nums)

    def putong(self, consum):
        print('1')
        rtnConsum = consum
        if consum >= 200:
            rtnConsum = 200 * 0.9
        if rtnConsum > consum:
            rtnConsum = consum
        return rtnConsum

    def vip(self, consum, nums):
        print('2')
        rtnConsum1 = consum
        rtnConsum2 = consum
        if consum >= 200:
            rtnConsum1 = consum * 0.8
        if nums >= 10:
            rtnConsum2 = consum * 0.85
        return min(rtnConsum1, rtnConsum2, consum)

#u1 = User(100, 10, 0) #0表示普通
#u2 = User(200, 20, 1) #1表示vip
#Settle(u1.type, u1.consum, u1.nums).panduan()
#Settle(u2.type, u2.consum, u2.nums).panduan()

s1 = Settle(100, 10, 0)
s2 = Settle(300, 30, 2)
s1.panduan()
#s2.panduan()