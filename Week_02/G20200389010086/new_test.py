########################
# 内置的装饰方法函数

# functools.wraps
# @wraps接受一个函数来进行装饰
# 并加入了复制函数名称、注释文档、参数列表等等的功能
# 在装饰器里面可以访问在装饰之前的函数的属性
# @functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
# 用于在定义包装器函数时发起调用 update_wrapper() 作为函数装饰器。
# 它等价于 partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)。
# wraps 加入后， 会把函数的名字、函数的参数列表、函数的注释文档替换回原有函数的名字，如下：test_arg 被替换为原有的函数名字（foo）


from time import ctime, sleep
from functools import wraps


def outer_arg(bar):
    def outer(func):
        # 结构不变增加wraps
        @wraps(func)
        def inner(*args, **kwargs):
            print("%s called at %s" % (func.__name__, ctime()))
            ret = func(*args, **kwargs)
            print(bar)

            return ret

        return inner

    return outer


@outer_arg('test_arg')
def foo(a, b, c):
    "““___doc___注释文档””"
    return (a + b + c)


print(foo(1, 2, 3))
