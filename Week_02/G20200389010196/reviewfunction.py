# def decorate(func):
#     print('running in module')
#     def inner():
#         return func()
#     return inner

# # 装饰器, @ 语法糖
# @decorate   
# def func():
#     print('do sth')
# func()
# 等效于下面
# def func():
#     print('do sth')
#func = decorate(func)

#func()

from time import ctime,sleep
def outer_arg(bar):
    def outer(func):
        print("在装饰foo，并不是foo 方法执行前")
        def inner(*args,**kwargs):
            print("foo 方法执行前")
            ret = func(*args,**kwargs)
            # print(bar)
            print("foo 方法执行后")
            return ret
        #print(inner)
        return inner
    return outer

@outer_arg('foo_arg')
def foo(a,b,c):
    print('foo 在调用')
    return (a+b+c)

# foo(1,3,5)

# outer_returned = outer_arg()
# inner_returned = outer_returned(foo)
# inner_returned(1,2,3)


# 相当于outer_arg('foo_arg')(foo)()
# 装饰器带参数，其实外加一层函数outer_arg，让装饰器的参数bar执行，定义函数装饰器本身outer且带原函数名foo来作参数，再返回装饰器本身outer函数对象，
# outer = outer_arg('foo_arg')
# 当装饰器outer执行时，定义了inner函数带原函数foo参数*args,**kwargs，inner函数里可执行原始函数foo, 执行原始函数foo前后都可以自定义一些逻辑。
# 再返回inner函数对象。
# inner = outer(foo)
# 此时原始函数名foo，已经更换成inner函数对象，执行inner函数
# inner() 

# 疑问
# 为什么执行原函数foo的逻辑喜欢写在 inner 里面而不是外层的 outer 呢, 是不是两者都可以
# 为什么 foo 明明换了inner 函数对象，而 inner 里面的却能执行原始的函数foo呢
# 因为 inner 函数定义是 执行的foo还是原地址的foo, 外层foo因为装饰器原因被换了地址 [foo = outer_arg('foo_arg')(foo)]

    



# import functools

# def log(func):
# #    @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# @log
# def test():
#     print('hello')
# test()
# print(test.__name__)
# partial底层看不懂

############################################
# 向一个函数添加属性
# def attrs(**kwds):
#     def decorate(f):
#         for k in kwds:
#             setattr(f, k, kwds[k])
#         return f
#     return decorate

# @attrs(versionadded="2.2",
#        author="Guido van Rossum")
# def mymethod(param):
#     pass
# a = mymethod(1)
# print(mymethod.__name__)


# 类装饰函数
# def wrapClass(cls):
#     def inner(a):
#         print('class name:', cls.__name__)
#         return cls(a)
#     return inner
 
# @wrapClass
# class Foo():
#     def __init__(self, a):
#         self.a = a
 
#     def fun(self):
#         print('self.a =', self.a)
 
 
# m = Foo('xiemanR')
# m.fun()


# from functools import wraps
 
# class MyClass(object):
#     def __init__(self, var='init_var', *args, **kwargs):
#         self._v = var
#         super(MyClass, self).__init__(*args, **kwargs)
    
#     def __call__(self, func):
#         print(123)
#         # 类的函数装饰器
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             func_name = func.__name__ + " was called"
#             print(func_name)
#             return func(*args, **kwargs)
#         return wrapped_function

# def my_print(param):
#     print(param)


# MyClass(100)(my_print)(1123)


# # 装饰类
# def decorator(aClass):
#     class newClass(object):
#         def __init__(self, args):
#             self.times = 0
#             self.wrapped = aClass(args)
#         def display(self):
#             self.times += 1
#             print("run times", self.times)
#             self.wrapped.display()
#     return newClass

# @decorator
# class MyClass(object):
#     def __init__(self, number):
#         self.number = number
#     def display(self):
#         print("number is",self.number)

# six = MyClass(6)
# for i in range(5):
#     six.display()

# def a():
#     pass
# print(a)