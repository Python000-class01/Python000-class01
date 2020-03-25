from decimal import Decimal

#订单类
class Order:
    def __init__(self, itemCount, amount):
        #商品数量
        self.itemCount = Decimal(itemCount)
        #订单金额
        self.amount = Decimal(amount)

#折扣规则基类
class Rule:
    def __init__(self, rule):
        self.rule = rule
    def calculate(self, order):
        return 1

#普通用户折扣规则1
class RuleNormal1(Rule):
    def __init__(self):
        self.rule = '普通用户消费不足 200 元，无折扣，原价付费;普通用户消费满 200 元打九折；'
    def calculate(self, order):
        return Decimal( 0.9 if order.amount >= 200 else 1 )

#VIP用户折扣规则1
class RuleVIP1(Rule):
    def __init__(self):
        self.rule = 'VIP 会员满 200 元打八折；'
    def calculate(self, order):
        return Decimal(0.8 if order.amount >= 200 else 1 )

#VIP用户折扣规则2
class RuleVIP2(Rule):
    def __init__(self):
        self.rule = 'VIP 会员满 10 件商品打八五折。'
    def calculate(self, order):
        return Decimal(0.85 if order.itemCount >= 10 else 1 )

#多规则处理
class RuleGroup:
    def __init__(self, ruleList):
        self.rule = '由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。'
        self.ruleList = ruleList
    def match(self, order):
        matchedRule = Rule('无规则')
        matchedRuleList = tuple(rule for rule in self.ruleList if rule.calculate(order) < 1)
        if (ruleLen := len(matchedRuleList)) == 1:
            matchedRule = matchedRuleList[0]
        elif ruleLen > 1:
            #大于1个规则符合时，使用折扣
            amountList = tuple( rule.calculate(order) for rule in matchedRuleList)
            matchedRule = matchedRuleList[amountList.index(min(amountList))]
        return matchedRule

#客户基类
class Customer:
    def __init__(self, level):
        self.level = level
    def createDiscount(self):
        return []

#普通客户类
class CustomerNormal(Customer):
    def __init__(self):
        self.level = 'NORMAL'
    def createDiscount(self):
        return [RuleNormal1()]

#VIP客户类
class CustomerVIP(Customer):
    def __init__(self):
        self.level = 'VIP'
    def createDiscount(self):
        return [RuleVIP1(), RuleVIP2()]

#支付类
class Payment:
    def pay(self, customer, order):
        #获取用户适用的规则类别
        ruleList = customer.createDiscount()
        #根据订单匹配规则
        matchedRule = RuleGroup(ruleList).match(order)
        #支付
        payment = order.amount * matchedRule.calculate(order)
        print(matchedRule.rule)
        print(f'{customer.level} customer item count { order.itemCount} amount {order.amount} pay { round(payment,2) }')

vip = CustomerVIP()
Payment().pay(vip, Order(5,100))
Payment().pay(vip, Order(10,100))
Payment().pay(vip, Order(10,200))
Payment().pay(vip, Order(15,200))
Payment().pay(vip, Order(15,300))

normal = CustomerNormal()
Payment().pay(normal, Order(5,200))
Payment().pay(normal, Order(5,100))
Payment().pay(normal, Order(15,100))

