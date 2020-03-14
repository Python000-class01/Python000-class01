# python 第一周总结
- [python 第一周总结](#python-%e7%ac%ac%e4%b8%80%e5%91%a8%e6%80%bb%e7%bb%93)
  - [python的基本用法](#python%e7%9a%84%e5%9f%ba%e6%9c%ac%e7%94%a8%e6%b3%95)
    - [变量](#%e5%8f%98%e9%87%8f)
      - [对象的拷贝](#%e5%af%b9%e8%b1%a1%e7%9a%84%e6%8b%b7%e8%b4%9d)
      - [序列](#%e5%ba%8f%e5%88%97)
      - [内置数据结构扩展模块collections](#%e5%86%85%e7%bd%ae%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84%e6%89%a9%e5%b1%95%e6%a8%a1%e5%9d%97collections)
    - [函数](#%e5%87%bd%e6%95%b0)
      - [LEGB原则](#legb%e5%8e%9f%e5%88%99)
      - [高阶函数](#%e9%ab%98%e9%98%b6%e5%87%bd%e6%95%b0)
      - [偏函数](#%e5%81%8f%e5%87%bd%e6%95%b0)
      - [函数参数类型](#%e5%87%bd%e6%95%b0%e5%8f%82%e6%95%b0%e7%b1%bb%e5%9e%8b)
    - [python中特有的一些例子](#python%e4%b8%ad%e7%89%b9%e6%9c%89%e7%9a%84%e4%b8%80%e4%ba%9b%e4%be%8b%e5%ad%90)
  - [requests库](#requests%e5%ba%93)
    - [python 基于requests实现http协议相关内容](#python-%e5%9f%ba%e4%ba%8erequests%e5%ae%9e%e7%8e%b0http%e5%8d%8f%e8%ae%ae%e7%9b%b8%e5%85%b3%e5%86%85%e5%ae%b9)
    - [动态网页获取webdriver in selenium](#%e5%8a%a8%e6%80%81%e7%bd%91%e9%a1%b5%e8%8e%b7%e5%8f%96webdriver-in-selenium)
  - [爬虫的解析网页工具库](#%e7%88%ac%e8%99%ab%e7%9a%84%e8%a7%a3%e6%9e%90%e7%bd%91%e9%a1%b5%e5%b7%a5%e5%85%b7%e5%ba%93)
    - [beautifulsoap](#beautifulsoap)
    - [lxml (xpath)](#lxml-xpath)
## python的基本用法
1. 了解python的长处，特点
- python有丰富的第三方库，编程过程中应善于站在巨人的肩膀上。
- python擅长做数据处理，爬虫等方面。

### 变量
- python中的变量
    + 可变类型 ：list,set,dict
    + 不可变类型 ：num,str,tuple
    + **可变和不可变的依据是变量所指向的内存地址处的值是不可以被改变的**
```python
# 不可变类型因为内存中数据不可变所以当数据被赋新值时内存即发生变化
a=1 a=2 #两次a的地址发生变化
# 同理可变类型其值发生变化会内存不会发生变化
a=[1,2,3] a[0]=2 #其地址不会发生变化
```
- 可变与不可变类型中的坑  
```python
x = [1,2,3]
y = x # y=x 进行了浅拷贝 y地址和x地址相同 
x[0]=3  x[1]=3  x[2]=3 # y也会跟着变化
x=[4,5,6] #x被指向了新的地址，y不会变化
```
- 元组是不可变类型
- 元组是个特例，值相同的元组的地址可能不同，因为它的本质是只读的列表
```python
# 元组是只读的列表
(1,3,[1,3,4]) ==>(1,3,[1,3,5])
# [1,3,4]是数组可变类型当其值变化时其地址不会变，故元组内部元素的地址没有变化所以是不可变类型
```
#### 对象的拷贝
- 参考
```
https://www.cnblogs.com/wilber2013/p/4645353.html
```
1. 赋值操作 =
    + 赋值操作拷贝出的新的对象所有元素对象都指向原来的元素
    + 原来地址内值变化两者都会变化(当然要遵循可变类型、不可变类型的特点)
    ```python
    will = ["Will", 28, ["Python", "C#", "JavaScript"]]
    wilber = will
    print id(will)
    print will
    print [id(ele) for ele in will]
    print id(wilber)
    print wilber
    print [id(ele) for ele in wilber]
    will[0] = "Wilber"
    will[2].append("CSS")
    # 每个元素的地址都相同
    ```
2. 浅拷贝 copy.copy /使用切片[:] / 使用工厂函数（如list/dir/set）
    + 浅拷贝会对原来对象中的原子元素创建一个完全独立新的对象，但对非原子元素则使用原来的地址引用
    ```python
    # 最后一个复杂元素改遍的时候会新元素会跟着变
    will = ["Will", 28, ["Python", "C#", "JavaScript"]]
    wilber = copy.copy(will)
    ```
3. 深拷贝
    + 深拷贝就是会对原来对象中的所有元素创建完全独立的新的对象
    ```python
    # 两个对象完全独立不会干扰
    will = ["Will", 28, ["Python", "C#", "JavaScript"]]
    wilber = copy.deepcopy(will)
    ```
4. 一些特殊情况
    + 对于不可变类型如何拷贝都会出现同地址的新对象
    + 对于全是原子元素的对象深拷贝和浅拷贝效果相同

#### 序列
    - 扁平序列 只能装同一种元素，如str
    - 容器序列 可装不同的元素，如列表，字典

#### 内置数据结构扩展模块collections

1. namedtuple
    + 可以是使用属性来访问的tuple
    + 不可变，方便访问
```python
Point = namedtuple('Ponits', ['x','y']) #初始化,第一个参数为typename 为元组子对象 一般与Point类名保持一致
p = Point(10, y=20)
p.x + p.y
p[0] + p[1]
x, y = p
# 获取某个值
getattr(p, 'x')

# 将dict转换为namedtuple
>>> d = {'x': 11, 'y': 22}
>>> Point(**d)
Point(x=11, y=22)
```

2. deque
    + 双向队列一般用于解决list删除插入等效率问题
```python
from collections import deque
d = deque('uvw')
d.append('xyz')
d.appendleft('rst')
```
3. Counter 
    + 用于做列表统计
```python
from collections import Counter
mystring = ['a','b','c','d','d','d','d','c','c','e']
# 取得频率座高的前三个值
cnt = Counter(mystring)
cnt.most_common(3)
cnt['b']
```
### 函数

#### LEGB原则
- 当函数调用时查找变量的顺序
```python
# L G
x = 'Global'
def func():
    x = 'Enclosing'
    def func2():
        x = 'Local'
        print (x)
    func2()
print(x)
func()
# E
x = 'Global'
def func3():
    x = 'Enclosing'
    def func2():
        return x
    return func2
var = func3()
print( var() )
# B
print (dir (__builtins__) )
```
#### 高阶函数
- map(func,iterator) 将func作用于iterator每个元素后返回iterator
```python
>>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
['1', '2', '3', '4', '5', '6', '7', '8', '9']
```
- reduce(func,iterator) reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
```python
from functools import reduce
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```
- filter(func,iterator) filter用于过滤，func用于返回bool类型变量，func依次作用于iterator元素上，返回结果为True的元素
```python
def is_odd(n):
    return n % 2 == 1
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]
```
#### 偏函数
- 一般用于将函数的某个参数固定,使函数更加简单
- 关于偏函数的参数问题，默认的从第一个参数开始
- 若定义偏函数时候使用了命名参数，则以后调用时候也要用命名参数
```python
from functools import partial
 
def mod( n, m ):
  return n % m
 
mod_by_100 = partial( mod, 100 ) # 默认代替的是第一个参数n
 
print mod( 100, 7 )  # 2
print mod_by_100( 7 )  # 2

mod_by_100 = partial( mod, m=100 ) # 命名方法定义
 
print mod( 100, 7 )  # 2
print mod_by_100( n=7 )  # 2
```

#### 函数参数类型
- 参考
```
liujiangblog.com/course/python/31
```
1. 必传参数 
```python 
# 比传参数必须按照顺序，不可省略
def add(a, b, c):
    return a+b+c

result = add("haha", 2,  3)

```
2. 默认参数
- 默认参数尽量指向不变的对象！
```python
# 默认参数会给参数一个默认值，传入时可省略
def power(x, n = 2):
    return x**n

ret1 = power(10)   # 使用默认的参数值n=2
ret2 = power(10, 4)  # 将4传给n，实际计算10**4的值
# 默认参数要在必传参数后面，多个默认参数传入时也许按照顺序
def student(name, sex, age, classroom="101", tel="88880000", address="..."):
    pass
student('jack','male',17)       # 其它全部使用默认值
student('tom','male',18,'102','666666','beijing')    # 全部指定默认参数的值
student('mary','female',18,'102',tel='666666')  # 挑着来
student('mary','female',18,tel='666666','beijing')   #  这是错误的参数传递方式
student("mary","female",18,tel="666666",address="beijing")

# 默认参数也可都使用命名参数的形式传递
def student(name, age, classroom, tel, address="..."):
    pass

student(classroom=101, name="Jack", tel=66666666, age=20)
```
3. 动态参数
    - 动态参数允许传入0或者n个参数
    - Python的动态参数有两种，分别是*args和**kwargs，这里面的关键是一个和两个星号的区别
    - 动态参数，必须放在所有的位置参数和默认参数后面！
    ```python 
    def func(name, age, sex='male', *args, **kwargs):
        pass
    ```
    1. *args
    ```python
       # 一个星号表示接收任意个参数。调用时，会将实际参数打包成一个元组传入形式参数。如果参数是个列表，会将整个列表当做一个参数传入
       # 使用* list 来分开传递list中的参数
        def func(*args):
            for arg in args:
            print(arg)

        li = [1, 2, 3]
        func(*li)
    ```
    2. **kwargs 两个星表示接受键值对的动态参数，数量任意。调用的时候会将实际参数打包成字典。
    ```python
    def func(**kwargs):
    for kwg in kwargs:
        print(kwg, kwargs[kwg])
        print(type(kwg))

    func(k1='v1', k2=[0, 1, 2])
    # 同理使用**kwargs进行参数传递会自动进行分割
    ```
### python中特有的一些例子
1. 推导式
    - 推导式是构建列表、字典、集合和生成器便捷方式
```python
字典推导式
mydict = {i: i*i for i in (5, 6, 7)}
集合推导式
myset = {i for i in 'HarryPotter' if i not in 'er'}
元组推导式要显式使用 tuple()，不能直接使用()
mytuple = tuple(i for i in range(10))
生成器
mygenerator = (i for i in range(0, 11))
```
2. 字符串格式化
    - f作为字符串格式化标识从python 3.6开始引入，方便，并且可换行
    ```
    ```
## requests库
- requests是一个很实用的Python HTTP客户端库，可以完全满足当今的网络需求
- 其简单易用，基于urllib3
- 安装
```python
# http://docs.python-requests.org/en/master/
pip install requests
```
### python 基于requests实现http协议相关内容

```python
r  = .get('http://httpbin.org/get')
# 传参 定制header
payload = {'key1': 'value1', 'key2': 'value2', 'key3': None}
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get('http://httpbin.org/get', params=payload,headers=headers)
# 基本属性
r.text #返回headers中的编码解析的结果，可以通过r.encoding = 'gbk'来变更解码方式
r.content #返回二进制结果
r.json() # 返回JSON格式，可能抛出异常
r.status_code
r.raw #返回原始socket respons，需要加参数stream=True 
```
- post
```python
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r.json()
```
- cookie相关
    + 一般来说通过post登录请求拿到访问网站所需cookie
    + 之后使用携带cookie的get请求来完成模仿浏览器
```python
# 基本用法
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r.cookie
response = requests.get(url3, headers = headers, cookies = r.cookies)
# session 用法
with requests.Session() as s:
    s.post('http://httpbin.org/cookies/set/')
    # 拿到cookie后会自动带上
    s.get('http://httpbin.org/cookies/set/')
```
- filedownload
```python
# 注意文件写入时需要使用wb
file = requests.get(fileurl)
with open("python_logo.png",'wb') as f:
    f.write(r.content)
# 分块
r = requests.get(file_url, stream=True)
with open("python.pdf", "wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)
```
- ssl
```python
# SSL 证书
# 如果你将 verify 设置为 False，Requests 也能忽略对 SSL 证书的验证。
requests.get('https://kennethreitz.org', verify=False)
# <Response [200]>

# 客户端证书
# 你也可以指定一个本地证书用作客户端证书，可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组：
requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))
# <Response [200]>
```

### 动态网页获取webdriver in selenium
- 
- 需要将下载的chrome模拟浏览器行为。
- chrome 基本用法很多
- webdriver可用于获取动态网页的内容 模拟浏览器的行为
- 下载对应版本的chrome driver 
- 每次操作完成后续进行浏览器关闭
- 国内很多网站已经禁用selenium
- 下载到的chromer diver
- webdriver可使用xpath进行DOM元素查找
```python
from selenium import webdriver
browser = webdriver.Chrome()
# 需要安装chrome driver
browser.get('https://www.douban.com')
# 基本代码
try:
    browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    btm1.click()

    browser.find_element_by_xpath('//*[@id="username"]').send_keys('15055495@qq.com')
    browser.find_element_by_id('password').send_keys('test123test123')
    time.sleep(1)
    browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()

    cookies = browser.get_cookies() # 获取cookies
    print(cookies)
except Exception as e:
    print(e)
finally:    
    browser.close()
```
## 爬虫的解析网页工具库
- beautifulsoap和lxml
- 其中lxml使用的是xpath的方式进行html元素的匹配，不需要像bs4那样将整个网页都进行格式化，速度更快

### beautifulsoap
- 官网
```
https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
```
- 特点: 支持链式编程、易用、支持CSS、
- 基本用法
1. 安装
```
pip install beautifulsoup4
```
2. 将reponse转换为beautifulsoap对象
```
bs_info = bs(response.text,"html.parser")
```
3. 基本步骤
```python
# 使用find_all选取元素,返回值为list[beautifulsoap] 
# 其中find() 方法返回为beautifulsoap类型
find_all( name , attrs , recursive , text , **kwargs )

# 使用attrs对tag属性进行筛选
bs_info.find_all('div',attrs={'id':'comments-section'})

# 使用get()对选中tag的属性进行获取
inner_url = info.find('a').get('href')

# 对tag中的text进行获取
text = info.find('a').string
```

### lxml (xpath)
- 官网
```
https://lxml.de/api.html#lxml-etree
```
- 基本用法
1. 安装
```
pip install lxml 
```
2. 将reponse xml化
```
# xml化处理
selector = lxml.etree.HTML(response.text)
```
3. 基本步骤
```python
# xpath 基本常用语法
# 其中// 为全局搜索 / 是其子元素  []谓语进一步增加筛选条件
# 返回类型为list [lxml.etree._Element] 类型
text = selector.xpath("//ol[@class='grid_view']/li[1]//a/span[1]")  
# 得到目标tag的lxml.etree._Element类型后可使用findall，getiterator等方法对其进行进一步获取
aaa=text[0].findall(path="./div[@class='info']/div/span[1]")[0].text
aaa=text[0].findall("span")[0].text
aaa1=list(text[0].getiterator(tag="span"))
#获取属性值或者text的值
xpath("//ol[@class='grid_view']/li[1]//a/span[1]/@href")  
aaa=text[0].findall("span")[0].text
```
4. 注意事项
```python
# 谓语条件一般只有一个，多个谓语会有一些莫名其妙的问题(待验证)
ol[@class='grid_view'][1]
```