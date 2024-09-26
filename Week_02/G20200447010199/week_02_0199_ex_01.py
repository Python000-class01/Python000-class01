class Person:
    # 会员名称
    name = ''
    # 会员类型（1.VIP会员 2.普通会员）
    type = 2
    # 结算密码
    pasword = ''
    # 应付金额
    _payAmount = 0
    def __init__(self,name,type,password):
        self.name = name
        self.type = type
        self.password = password
    def __str__(self):
        print("name:%s;type:%s;"%(self.name,self.type))
    def compute(self,amount,count):
        if self.type == 1:
            if amount >= 200:
                self._payAmount = amount * 0.8
            elif count >= 10:
                self._payAmount = amount * 0.85
            else:
                self._payAmount = amount
        if self.type == 2:
            if amount >= 200:
                self._payAmount = amount * 0.9
            else:
                self._payAmount = amount
    def get_pay_amount(self):
        return "应付金额为:%d"%(self._payAmount)

person = Person('jordan',2,'123456')
person.compute(300,3)
print(person.get_pay_amount())
