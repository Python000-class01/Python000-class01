class consumer(object):
    def __init__(self, name):
        self.name = name
        self.basket = list()

# 对商品的操作这里直接输入价钱,方便操作
    def shopping(self, item):
        self.basket.append(item)

    # def throw(self, item):
    #     self.basket.remove(item)

    def cost(self):
        # print(self.__class__)
        base_cost = sum(self.basket)
        if self.__class__.__name__ == 'normal':
            if base_cost < 200:
                cost = base_cost
            if base_cost >= 200:
                cost = base_cost*0.9
        if self.__class__.__name__ == 'vip':
            tmp_list = []
            if base_cost >= 200:
                tmp_list.append(base_cost*0.8)
            if len(self.basket) >= 10:
                tmp_list.append(base_cost*0.85)
            tmp_list.append(base_cost)
            tmp_list.sort()
            cost = tmp_list[0]
        print(f'消费了{cost}')
        print('bye')


class vip(consumer):
    def __init__(self, name):
        super().__init__(name)


class normal(consumer):
    def __init__(self, name):
        super().__init__(name)


class store(object):
    def get_con(self, name, viplevel):
        if viplevel == 0:
            return normal(name)
        return vip(name)


if __name__ == '__main__':
    store = store()
    npc1 = store.get_con('L5', 1)
    npc1.shopping(100)
    npc1.shopping(220)
    npc1.cost()
