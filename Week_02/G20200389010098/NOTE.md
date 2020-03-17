带参数的装饰器多包了一层  
wrapt完善的装饰器  
functools.lru_cache可以缓存函数结果，在运算复杂的递归函数中特别有用  
functools.lru_cache(maxsize=128, typed=False)有两个可选参数  
maxsize代表缓存的内存占用值，超过这个值之后，就的结果就会被释放  
typed若为True，则会把不同的参数类型得到的结果分开保存  
可以用类去装饰函数  
装饰类一定要用类  
向一个函数添加属性  
```
def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f
    return decorate
@attrs(versionadded="2.2",
       author="Guido van Rossum")
def mymethod(f):
    pass
```
dataclass可以简化类的普通字段的定义  
静态变量：类中定义不带self的变量，可在类以外定义 
静态变量每个实例都有一份，相互不干扰  
内置类型不能直接增加属性和方法  
私有变量用 __定义 会自动改名成_Human2__fly，但其实还是很访问  
\__getattribute__返回存在的属性，如果不存在抛出  AttributeError 异常，继续访问getattr__函数  
如果同时存在，执行顺序是getattribute__>getattr__>dict__  
python中，一个类实现了\__get__, \__set__，\__delete__的三个方法中的任意一个就是描述器  
1.如果仅仅实现了\__get__.就是非数据描述器 non-data descriptor  
2.同时实现了\__get__,\__set__,就是数据描述器，data descriptor  
如果一个类的类属性，设置为描述器，那么这个类被称为owner属主，method也是类的属性  
用描述器可以对传入值的类型范围做限制  
property 可以将复杂的逻辑作为属性返回，property的setter和deleter的方法名最好相同  
property经典场景可以用来判断状态，和偏函数结合可以做公有云分发
property的方法改写成 \_Article__gender  
@classmethod 可以将类的方法静态化，可以不实例话就直接调用，但是self要换成cls  
@staticmethod 不传入self 也不传入 cls，所以不能使用类属性和实例属性。一般作为和类有关系的独立函数使用，保持统一管理  
werkzeug.utils 的 cached_property 可以实现类方法的缓存，flask里也多有用到  
子类要继承父类的属性要在\__init__里super  
super().__init__(name)  
super(Man, self).__init__()  
type元类由type自身创建，object类由元类type创建  
type类继承了object类  
所有都是由type创建  
所有都继承自object  
多继承，可以用.mro()查看继承顺序，左侧追述到和右侧同一个父为止  
没有多态，同名函数会被覆盖  
1.\__init__ 通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后。它是实例级别的方法。  
2.\__new__ 通常用于控制生成一个新实例的过程。它是类级别的方法。  
https://www.cnblogs.com/shenxiaolin/p/9307496.html  
工厂模式可以在函数内动态创建的类  
```
def factory2(func):
    class klass: pass
    #setattr需要三个参数:对象、key、value
    setattr(klass, func.__name__, func )
    return klass
def say_foo(self): print('bar')
Foo = factory2(say_foo)
foo = Foo()
foo.say_foo()
```
使用type 元类创建类  
```
def hi():
    print('Hi metaclass')
Foo = type('Foo',(),{'say_hi':hi})
foo = Foo
foo.say_hi()
```
Mixin可以理解为python的接口  
```
MySubClass(LoggerMixin,Displayer)
```
Displayer定义接口，Mixin具体实现  
metaclass可以扩展内置数据类型，赋予新的方法 