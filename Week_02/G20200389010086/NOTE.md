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
# 属性装饰器 @property
#@property 可以把一个实例方法变成其同名属性，以支持实例访问，它返回的是一个property属性；,相当于调用属性一样调用类中的方法
import math
class Circle:
    def __init__(self,radius): #圆的半径radius
        self.radius=radius

    @property
    def area(self):
        return math.pi * self.radius**2 #计算面积
    @property
    def perimeter(self):
        return 2*math.pi*self.radius #计算周长
        
circle=Circle(10)
print(circle.radius)
print(circle.area) 
print(circle.perimeter

# @classmethod   修饰的方法不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等.也就是说，类中使用 @classmethod 修饰的方法，该方法在调用过程中，可以不实例化类，直接调用。

class A():
    number = 10
    @classmethod
    
    def get_a(cls):     #cls 接收的是当前类，类在使用时会将自身传入到类方法的第一个参数
        print('这是类本身：',cls)# 如果子类调用，则传入的是子类
        print('这是类属性:',cls.number)

class B(A):
    number = 20
    pass

# 调用类方法 不需要实例化可以执行调用类方法
A.get_a()
B.get_a()


# @staticmethod：改变一个方法为静态方法，静态方法不需要传递隐性的第一参数，静态方法的本质类型就是一个函数 一个静态方法可以直接通过类进行调用，也可以通过实例进行调用
import time
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    @staticmethod
    def now(): #用Date.now()的形式去产生实例,该实例用的是当前时间
        t=time.localtime() #获取结构化的时间格式
        return Date(t.tm_year,t.tm_mon,t.tm_mday) #新建实例并且返回


    @staticmethod
    def tomorrow():#用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
        t=time.localtime(time.time()+86400)
        return Date(t.tm_year,t.tm_mon,t.tm_mday)
    
a=Date('1987',11,27) #自己定义时间
print(a.year,a.month,a.day)
b=Date.now() #采用当前时间
print(b.year,b.month,b.day)
c=Date.tomorrow() #采用明天的时间
print(c.year,c.month,c.day)

# 类的实例化
# __getattr__ 返回所有属性
# __getattribute__ （属性存在或不存在都会执行），拦截已存在的属性，如果不存在抛出  AttributeError 异常，继续访问__getattr__函数
# 可以根据原理改造 __getattribute__ 实现 __getattr__
# 如果同时存在，执行顺序是 __getattribute__ > __getattr__ > __dict__











