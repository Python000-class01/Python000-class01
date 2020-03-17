# in: item prices[], out {count, price}
def get_sum(items_prices):
    count = 0
    prices = 0
    for item_price in items_prices:
        count = count + 1
        prices = prices + item_price
    return {'count': count, 'prices': prices}


class Calculator(object):
    def __init__(self, common_rule, vip_rule):
        self.common_rule = common_rule
        self.vip_rule = vip_rule

    def discount(self, items_prices, is_vip):
        result = get_sum(items_prices)
        print(result)
        count = result['count']
        prices = result['prices']
        if is_vip:
            return self.vip_rule(count, prices)
        else:
            return self.common_rule(count, prices)
