学习笔记
# 函数的定义中， 默认参数，一定要定义为不可变参数也就是不可变对象, 可变参数 也就是参数的个数可变，如下
`def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3))
print(calc(2, 3))`