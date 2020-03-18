class Customer(object):
    def __init__(self):
        self.kind = None
        self.grocery = None
        self.amount = None

class NormalCustomer(Customer):
    def __init__(self, grocery, amount):
        print(f'This is a normal customer, buy {grocery} groceries, cost {amount}')

class VipCustomer(Customer):
    def __init__(self, grocery, amount):
        print(f'This is a vip customer, buy {grocery} groceries, cost {amount}')

class Factory:
    def getAmount(self, kind, grocery, amount):
        if kind == 'Normal':
            if amount >= 200:
                amount = amount * 0.9
            return NormalCustomer(grocery, amount)
        elif kind == 'Vip':
            if amount >= 200: #“满200元”和“满10件商品”，肯定8折便宜
                amount = amount * 0.8
            elif grocery >= 10:
                amount = amount * 0.85
            return VipCustomer(grocery, amount)
        else:
            raise TypeError(f'客户类型错误：{kind}')

if __name__ == '__main__':
    factory = Factory()
    customerKind = input("请输入客户类型：Normal or Vip?\n")
    grocery = input("请输入购买的商品数量：\n")
    amount = input("请输入购买的原商品总金额：\n")
    factory.getAmount(customerKind, int(grocery), float(amount))

