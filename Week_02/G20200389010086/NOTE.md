学习笔记
# 函数的定义中， 默认参数，一定要定义为不可变参数也就是不可变对象, 可变参数 也就是参数的个数可变，函数中，参数前加“*”， 如下
`def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3))
print(calc(2, 3))


def func():
    pass
# func  表示函数， func() 表示执行函数（调用运行）
# 装饰器 在模块导入的时候自动运行
# 装饰器堆叠
#类装饰器， 装饰器中的方法， 要和类中的方法名一样








