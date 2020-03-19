学习笔记
###### 函数属性
```python
#提取函数中''' '''的内容为文档
print(my_line.__doc__)
# 编译后函数体保存的局部变量
print(my_line.__code__.co_varnames)
# 编译后函数体保存的自由变量
print(my_line.__code__.co_freevars)
# 自由变量真正的值
print(my_line.__closure__[0].cell_contents)
#函数还有哪些属性
print(dir(line_conf()))
#函数名
print(line_conf.__name__)
```

###### 如果闭包要引用外部函数的局部变量则需要使用nonlocal 变量名称，否则不可使用
```python
def counter2(start=0):
    def incr():
        nonlocal start
        start+=1
        return start
    return incr
```

###### LEGB
>命名空间是对变量名的分组划分。
不同组的相同名称的变量视为两个独立的变量，因此隶属于不同分组（即命名空间）的变量名可以重复。命名空间可以存在多个，使用命名空间，表示在该命名空间中查找当前名称。
>由于Python一切皆对象，所以在Python中变量名是字符串对象。Python的命名空间是一个字典，字典内保存了变量名称与对象之间的映射关系。因此，查找变量名就是在命名空间字典中查找键-值对。LEGB就是用来规定命名空间查找顺序的规则。
>LEGB含义解释：
>* L-Local(function)；函数内的名字空间
>* E-Enclosing function locals；外部嵌套函数的名字空间(例如closure)
>* G-Global(module)；函数定义所在模块（文件）的名字空间
>* B-Builtin(Python)；Python内置模块的名字空间