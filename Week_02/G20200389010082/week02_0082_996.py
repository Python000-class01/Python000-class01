# _*_ coding: utf-8 _*_


class super_996(object):
    def __init__(self):
        self.__goodsPrice = {"美国艾尔": 40, "英国艾尔": 45, "德国小麦": 50, "比利时酸": 67, "中国水": 20, "苏格兰威": 100, "日本威": 90, "美国石": 80, "其他": 150}  # 商品及价目

    @property
    def checkout(self):
        return self._checkout

    @checkout.setter
    def checkout(self, custom_info):
        pay = 0  # 初始化金额
        for foods in custom_info["foods_list"]:  # 提取货品，累加计算
            if foods in self.__goodsPrice:
                pay += self.__goodsPrice[foods]
        if custom_info["is_vip"] is True:  # 确认客户等级 VIP

            if pay >= 200 and len(custom_info["foods_list"]) >= 10:
                if pay * 0.8 > pay * 0.85:
                    pay = pay * 0.8
                else:
                    pay = pay * 0.85

            if pay >= 200:  # 大于200块 八折
                pay = pay * 0.8
            if len(custom_info["foods_list"]) >= 10:  # 大于10件产品
                pay = pay * 0.85

        else:
            if pay >= 200:
                pay = pay * 0.9

        self._checkout = pay

if __name__ == '__main__':
    super9 = super_996()
    super9.checkout = {"is_vip": True, "foods_list": ['英国艾尔', '美国艾尔', '日本威','日本威','日本威','日本威','日本威','日本威','日本威','日本威', '其他']}
    print(super9.checkout)


