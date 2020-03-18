# -*- encoding=utf-8 -*-
# @File: week02_0108_ex2.py
# @Author：wsr
# @Date ：2020/3/17 18:24

# 不带参数函数装饰器
def tips(func):
    def nei_func(param1, param2):
        print('startting...')
        # 函数部分
        func(param1, param2)
        # 结束的部分
        print('stopped')

    return nei_func


@tips
def add(a, b):
    print(a + b)


print(add(3, 4))


# 带参数函数装饰器
def new_tips(argv):
    def tips(func):
        def nei_func(param1, param2):
            print('start %s %s' % (argv, func.__name__))
            # 函数部分
            func(param1, param2)
            # 结束的部分
            print('stop')

        return nei_func

    return tips


# 加法
@new_tips('add_v2')
def add_v2(a, b):
    print(a + b)


print(add_v2(3, 4))


def outer(clss):  # 类装饰器
    class Inner(object):
        msg = 'test_msg'

        def __init__(self):
            self.clss = clss()

        def __getattr__(self, attr):
            return getattr(self.clss, attr)

        def __call__(self):
            self.name = 'warp'

    return Inner


@outer
class TestClass(object):
    def __init__(self):
        pass


test = TestClass()
print(test.msg)
