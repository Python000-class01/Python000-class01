# I have a dream
class MyFirstClass:
    pass
a = MyFirstClass()
b = MyFirstClass()

# 不同内存地址，两个不同对象
type(a)
id(a)
a.__class__()
b.__class__()

# 类也是对象
c = MyFirstClass
d = c()
d.__class__()

##########################
# GOD
class Human(object):
    # 静态字段
    live = True

    def __init__(self, name):
        # 普通字段
        self.name = name

man = Human('Adam')
woman = Human('Eve')

# 有live属性
Human.__dict__
# 有name属性
man.__dict__

# 实例可以使用普通字段也可以使用静态字段
man.name
man.live = False
print(man.__dict__) #普通字段有live变量
# man.live
# woman.live

# # 类可以使用静态字段
# Human.live

# # 可以为类添加静态字段
# Human.newattr = 1
# dir(Human)
# Human.__dict__

# # 内置类型不能增加属性和方法
# setattr(list, 'newattr', 'value')
# # TypeError


# #########################
# class Human2(object):
#     # 人为约定不可修改
#     _age = 0

#     # 私有属性
#     __fly = False

#     # 魔术方法，不会自动改名
#     # 如 __init__


# # 自动改名机制
# Human2.__dict__
