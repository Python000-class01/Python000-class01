# 女娲
class Human(object):
    def __init__(self, name):
        self.name = name

h1 = Human('Adam')
h2 = Human('Eve')


# 对实例属性做修改
h1.name = 'python'
h1.name
h2.name
# 删除实例属性
del h1.name

# AttributeError
# 访问不存在的属性
h1.name

# 对属性进行拦截
# 女娲
class Human(object):
    def __init__(self, name):
        self.name = name
    def __getattr__(self, item):
        print('Human:__getattr__')
        return 100

    # def __getattribute__(self, item):
    #     print('Human:__getattribute__')
    #     try:
    #         return super().__getattribute__(item)
    #     except Exception as e:
    #         self.__dict__[item] = 100
    #         return 100



h1 = Human('Adam')
h2 = Human('Eve')
# __getattr__ 拦截任意属性
# __getattribute__ 返回存在的属性，如果不存在抛出  AttributeError 异常，继续访问__getattr__函数
# 可以根据原理改造 __getattribute__ 实现 __getattr__
# 如果同时存在，执行顺序是 __getattribute__ > __getattr__ > __dict__


