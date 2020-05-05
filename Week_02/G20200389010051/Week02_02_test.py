#复习函数装饰器、类装饰、装饰器带参数与魔术方法的功能，参考官方文档熟悉魔术方法对应的 Python 内置方法。
#参考网站： https://docs.python.org/zh-cn/3.7/reference/datamodel.html

def decorate(func):
    def inner():
        print('in decorate')
        func()
    return inner

@decorate
def target():
    print('do something')

target()

