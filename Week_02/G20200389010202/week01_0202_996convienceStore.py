# 便利店
class ConvienceStore(object):
    product_name = ["矿泉水", "面包", "可乐", "薯片"]
    product_price = [2, 4, 2.5, 3.5]
    product_list = dict(zip(product_name, product_price))

    def __init__(self, name):
        self.store_name = name
        print(f"欢迎来到{name}便利店，今天开业啦！")
        print("现开业大酬宾，任意消费满200元打九折，办理会员可享更多优惠！")

    # 进货-定价
    def purchasing(self, product, price):
        if product in self.product_name:
            print(f"{product}已经在售")
        else:
            self.product_name.append(product)
            self.product_list[product] = price
            print(f"{product}为新产品，现售价{price}元")
        return self.product_list

    # 结算

    def counting(self, shopping_list):
        total = 0
        amount = 0

        for product, number in shopping_list.items():
            if product in self.product_name:
                total += self.product_list[product] * number
                amount += number
            else:
                print(f"抱歉, {product}暂未销售")
                continue

        return total, amount


# 便利店的普通顾客
class Customer(object):
    def __init__(self, name):
        self.customer_name = name
        print(f"欢迎光临，{name}")
        self.customer_rank = "normal"

    # 付钱
    def paying(self, *bill):
        if total >= 200:
            payment = total * 0.9
        else:
            payment = total

        print(f"亲爱的顾客{self.customer_name}，您需要支付{payment:.2f}元") # 去掉小数后多余数字


# 便利店的VIP顾客
class VIPCustomer(Customer):
    def __init__(self, name):
        super().__init__(name)
        self.customer_rank = "VIP"

    def paying(self, *bill): #父类Customer的paying方法传一个参数，子类VIPCustomer的paying方法不能传两个参数？不明白
        if total < 200:
            if amount >= 10:
                payment = total * 0.85
            else:
                payment = total
        else:
            payment = total * 0.8

        print(f"尊贵的会员{self.customer_name}，您需要支付{payment:.2f}元")


# 创建便利店
myStore = ConvienceStore("996")
# 创建顾客
normal_customer = Customer("AMY")
VIP_customer = VIPCustomer("David")
# 结算
# shopping_list = {"可乐": 80, "巧克力": 2, "薯片": 3}
shopping_list = {"矿泉水": 6, "巧克力": 2, "薯片": 3}
total = myStore.counting(shopping_list)[0]
amount= myStore.counting(shopping_list)[1]
# 付款
normal_customer.paying(total)
VIP_customer.paying(total, amount)

# 进货
myStore.purchasing("巧克力", 6)
# 重新结算和付款
total = myStore.counting(shopping_list)[0] # 为什么变量名要跟paying方法里的变量名一样？
amount = myStore.counting(shopping_list)[1]
normal_customer.paying(total)
VIP_customer.paying(total, amount)

# print(myStore.product_list)


