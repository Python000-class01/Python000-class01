from calculator import Calculator
from rules import vip_rule, common_rule

calculator = Calculator(common_rule, vip_rule)

item_prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

result = calculator.discount(item_prices, True)
print(result)