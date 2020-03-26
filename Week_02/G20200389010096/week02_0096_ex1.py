from dataclasses import dataclass
from random import random


@dataclass
class Merchandise:
    name: str
    price: float
    def buy(self, count) -> float:
        cost = self.price * count
        return cost


class Store996:
    def __init__(self, typeCount):
        self.merchandises = list()
        self.typeCount = typeCount
        for i in range(self.typeCount):
            name = f'M-{i}'
            price = round((random() * 80), 1)
            self.merchandises.append(Merchandise(name, price))


def main(store):
    m = store.merchandises
    totalCount = 0
    totalCost = 0

    print(f'尊敬的顾客您好，欢迎惠顾996便利店，现在开始为您结算商品')
    while(True):
        mId = int(input('请输入您要结算的商品编号（1-100，结束请输0）：'))
        if mId > 0 and mId <= 100:
            print(f'这件商品的单价为 {m[mId-1].price} 元')
            mCount = int(input('请输入您要购买的数量：'))
            while(mCount <= 0):
                mCount = int(input('您输入的数量有误，请重新输入：'))
            mCost = m[mId-1].buy(mCount)
            print(f'您购买这件商品将花费 {mCost} 元')
            totalCount += mCount
            totalCost += mCost
        elif mId < 0 or mId > 100:
            print('抱歉，您输入的商品编号不存在，请重新输入')
            continue
        else:   # mId == 0
            break

    if totalCount > 0:
        print('现在开始为您结账')
        isVIP = int(input('请问您是否是VIP（1为是，0为否）：'))
        if isVIP == 1:
            if totalCost >= 200:
                totalCost *= 0.8
            elif totalCount >= 10:
                totalCost *= 0.85
        else:
            if totalCost >= 200:
                totalCost *= 0.9
        totalCost = round(totalCost, 1)
        print(f'您一共购买 {totalCount} 件商品，共花费 {totalCost} 元')

    print('非常感谢您的惠顾，欢迎再次光临996便利店，祝您生活愉快！')


if __name__ == '__main__':
    store = Store996(100)
    main(store)