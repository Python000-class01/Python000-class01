# Python 面向对象

## 新式类的继承、重载、多态

Python 的新式类与经典类

注意：在 Python3 中都是新式类。

```python
class MyFirstClass:
	pass

a = MyFirstClass()
b = MyFirstClass()

type(a)
id(a)
a.__class__() # 当前操作的对象属于哪个类

# 类也是对象
c = MyFirstClass
d = c()
```

### 属性和方法

类属性和对象属性：

```python
class Human(object):
    # 类属性（静态字段），在内存只保存一份
    live = True
    def __init__(self, name):
        # 对象属性（普通字段），为每个对象都保存一份
        self.name = name

# 实例化
man = Human('Adam')
woman = Human('Eve')

# 查看所有类属性和对象属性
Human.__dict__
man.__dict__

# 实例可以使用类属性，也可以“修改”类属性
man.live
man.live = False
man.__dict__
man.live
woman.live

# 类可以使用类属性
Human.live
# 也可以为类添加静态字段
Human.newattr = 1
dir(Human)
Human.__dict__

# setattr()可以为对象添加属性，但不能操作内置类型，会报TypeError
setattr(list, 'newattr', 'value')
```

属性的命名：

```python
class Human2(object):
	# 认为约定不可修改
    _age = 0
    # 私有属性，会被自动改名
    __fly = False
    # 自定义名称，防止与关键字重名
    list_ = [1, 2]
    # 魔术方法，不会自动改名
    __init__(self):
        pass
```

方法：

```python
class Human(object):
    # 使用__init__接收参数，思考不定参数处理
    def __init__(self, name):
        # self表示对象本身，约定俗成
        self.name = name

h1 = Human('Adam')
h2 = Human('Eve')

# 修改实例属性
h1.name = 'python'
# 查询实例属性
h1.name
# 删除实例属性
del h1.name
# 访问不存在的属性会报 AttributeError
h1.name
```

### 描述器

拦截属性：

```python
class Human(object):    
    def __init__(self, name):
        self.name = name
    
    # __getattr__ 拦截不存在的属性（__setattr__、__delattr__）
    # def __getattr__(self, item):
    #     print('Human:__getattr__')
    #     return 100
    
    # __getattribute__ 拦截任意属性，如果不存在抛出  AttributeError 异常，继续访问__getattr__函数
    # 可以根据原理改造 __getattribute__ 实现 __getattr__
    # 如果同时存在，执行顺序是 __getattribute__ > __getattr__ > __dict__
    def __getattribute__(self, item):
        print('Human:__getattribute__')
        try:
            return super().__getattribute__(item)
        except Exception as e:
            self.__dict__[item] = 100
            return 100

h1 = Human('Adam')
h2 = Human('Eve')

h1.fly
```

底层原理：

```python
# __getattribute__ 的底层原理是描述器（实现特定协议的类）
class Desc(object):
    """
    通过打印来展示描述器的访问流程
    """
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f'__get__{instance} {owner}')
        return self.name

    def __set__(self, instance, value):
        print(f'__set__{instance} {value}')
        return self.name

    def __delete__(self, instance):
        print(f'__set__{instance}')
        return self.name

class MyObj(object):
    a = Desc('aaa')
    b = Desc('bbb')

if __name__ == "__main__":
    inst = MyObj()
    print(inst.a)
    inst.a = 456
    print(inst.a)
```

```python
# __getattribute__ 纯python的实现
def __getattribute__(self, key):
    "Emulate type_getattro() in Objects/typeobject.c"
    v = object.__getattribute__(self, key):
    if hasattr(v, '__get__'):
        return v.__get__(None, self)
    return v
```

@property 将方法封装成属性

```python
class Human(object):
    def __init__(self):
        self._gender = None
    # 将方法封装成属性
    @property
    def gender(self):
        print(self.gender)

    # 支持修改
    @gender.setter
    def gender(self,value):
        self.gender = value

    # 支持删除
    @gender.deleter
    def gender(self):
        del self.gender


h = Human()
h.gender = 'F'
h.gender

# 另一种property写法
# gender  = property(get_, set_, del_, 'other property')

# 不使用setter并不能真正意义上实现无法写入，gender被改名为 _Article__gender
```

底层实现：

```python
"Emulate PyProperty_Type() in Objects/descrobject.c"
```

类方法：

```python
class A(object):
    bar = 1
    def foo(self):
        print('in foo')
    # 使用类属性、方法
    @classmethod
    def class_foo(cls):
        print(cls.bar)
        cls().foo()

A.class_foo()

# 示例
class Story(object):
    snake = 'Python'
    def __init__(self, name):
        self.name = name
    # 类的方法
    @classmethod
    def get_apple_to_eve(cls):
        return cls.snake
    
if __name__ == '__main__':
    s = Story('anyone')
    # get_apple_to_eve 是bound方法，查找顺序是先找s的__dict__是否有get_apple_to_eve,如果没有，查类Story
    print(s.get_apple_to_eve)
    # 类和实例都可以使用
    print(s.get_apple_to_eve())
    print(Story.get_apple_to_eve())
    print(type(s).__dict__['get_apple_to_eve'].__get__(s,type(s)))
    print(type(s).__dict__['get_apple_to_eve'].__get__(s,type(s)) == s.get_apple_to_eve)
```

静态方法：

```python
import datetime
class Story(object):
    snake = 'Python'
    def __init__(self, name):
        self.name = name
    # 静态方法
    @staticmethod
    def god_come_go():
        if datetime.datetime.now().month % 2 :
             print('god is coming')
    
Story.god_come_go()
# 静态方法可以由类直接调用
# 因为不传入self 也不传入 cls ，所以不能使用类属性和实例属性
```

描述器的案例：

```python
#1 实现缓存功能
from werkzeug.utils import cached_property
# werkzeug.utils.py p53
class Foo(object):
    @cached_property
    def cal(self):
        print('show me one time')
        var1 = 'cached info'
        return var1

bar = Foo()
bar.cal
bar.cal

#2 ORM(flask.ext.sqlalchemy)
# 一个表记录一个节点的心跳更新
# 通过一个属性来获取节点是否可用，而不用写复杂的查询语句
class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    updated_at = db.Column(db.DateTime) # 节点最后心跳时间
    state = db.Column(db.Integer, nullable=False) # 节点是否禁用

    @property
    def is_active(self):
        if(datetime.datetime.now() - self.updated_at).secondes > 60 \
            and self.vm_state == 0:
            return False
        return True

#3 限制传入的类型和范围（整数，且满足18-65）
class Age(object):
    def __init__(self, default_age = 18):
        self.age_range = range(18,66)
        self.default_age = default_age
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default_age)
    
    def __set__(self, isinstance, value):
        if value not in self.age_range:
            raise ValueError('must be in (18-65)')

        self.data[isinstance] = value

class Student(object):
    age = Age()

if __name__ == '__main__':
    s1 = Student()
    s1.age = 30
    s1.age = 100

#4 固定部分传递的参数
def xxyun_client(apitype, ak, sk, region='cn-beijing-3'):
    s = get_session()
    client = s.create_client(
        apitype,
        region,
        user_ssl = True,
        access_key =ak,
        secret_access_key =sk
    )
    return client

class XXYunBase(object):
    def __init__(self, account):
        self.account = account
        self.ak = self.account.ak
        self.sk = self.account.sk
    
    @property
    def eip_(self):
        return partial(xxyun_client, 'eip', self.ak, self.sk)
    
    @property
    def vpc_(self):
        return partial(xxyun_client, 'vpc', self.ak, self.sk)

#5 获取当前状态
@property
def current_state(self):
    instance_state = {
       1: '运行',
       2: '离线',
       3: '下线',
   } 
    if(time_diff.seconds) >= 300:
       return instance_state[2]

    if self.state in range(10):
        return instance_state.get(self.state, '其他')
    return None 
```

描述器协议：`__get__、__set__、__delete__`

描述器实现：`__getattr__、__setattr__、__delattr__、__getattribute__、property、staticmethod、classmethod`

## 面向对象

### 继承

```python
# 父类
class People(object):
    def __init__(self, name):
        self.gene = 'XY'
        # 假设人人都有名字
        self.name = name
    def walk(self):
        print('I can walk')

# 子类
class Man(People):
    def __init__(self,name):
        # 找到Man的父类People，把类People的对象转换为类Man的对象
        super().__init__(name)

    def work(self):
        print('work hard')

class Woman(People):
    def __init__(self,name):
        super().__init__(name)
    def shopping(self):
        print('buy buy buy')

p1 = Man('Adam')
p2 = Woman('Eve')

# 问题1 gene有没有被继承？
# super(Man,self).__init__()

# 问题2 People的父类是谁？
# object 与 type
print('object', object.__class__, object.__bases__)
print('type', type.__class__, type.__bases__)
# type元类由type自身创建，object类由元类type创建
# type类继承了object类

# 问题3 能否实现多重层级继承
# 问题4 能否实现多个父类同时继承 
class Son(Man, Woman):
    pass
# 新的问题： 继承顺序（钻石继承）
```

### 多态

鸭子类型

### 重载

```python
class  Klass(object):
    def A(self):
        pass
    def A(self,a, b):
        print(f'{a},{b}')

inst = Klass()
# 没有实现重载
inst.A()
```



## 设计模式

### 单例模式

```python
# 装饰器实现单实例模式
def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton 
class MyClass:
    pass

# __new__
class Singleton2(object):
	__isinstance = False  # 默认没有被实例化
	def __new__(cls, *args, **kwargs):
		if cls.__isinstance:  
			return cls.__isinstance  # 返回实例化对象
		cls.__isinstance = object.__new__(cls)  # 实例化
		return cls.__isinstance
```

### 工厂模式

```python
class Human(object):
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

class Man(Human):
    def __init__(self, name):
        print(f'Hi,man {name}')

class Woman(Human):
    def __init__(self, name):
        print(f'Hi,woman {name}')

class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Man(name)
        elif gender == 'F':
            return Woman(name)
        else:
            pass

if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("Adam", "M")
```

### 元类

```python
# 使用type 元类创建类
def hi():
    print('Hi metaclass')

Foo = type('Foo',(),{'say_hi':hi})
foo = Foo
foo.say_hi()
```

































