class Consumer:
    def __init__(self, num, total_price):
        self.num = num
        self.total_price = total_price

class Normal(Consumer):
    def __init__(self, num, total_price):
        result = total_price
        if total_price >= 200:
            result *= 0.9
        print(f"Normal: {result}")

class VIP(Consumer):
    def __init__(self, num, total_price):
        result1 = total_price
        result2 = total_price
        if total_price >= 200:
            result1 *= 0.8
        if num >= 10:
            result2 *= 0.85
        result = result1
        if result2 < result1:
            result = result2
        print(f"VIP: {result}")

class Calculation:
    def getResult(self, type, num, total_price):
        if type == 'VIP':
            return VIP(num, total_price)
        if type == 'Normal':
            return Normal(num, total_price)

if __name__ == '__main__':
    calculation = Calculation()
    calculation.getResult("VIP", 3, 190)