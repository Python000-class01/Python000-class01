##  <center> 学习笔记 </center>

1. 提交作业需要使用github、git，把以前学的一点知识捡了起来：

```
    git clone "SSH 或 HTTPS"

    git add .

    git commit -m "备注"

    git reset (commit序列)

    git push

    git pull

    git config --global user.name ""

    git config --global user.email ""

    git log
    
    git status
```

2. 课堂上也学习了许多：
- 使用requests库，访问url
```python
    #url是需要访问的地址，headers是你想要传递的请求头
    #如果resopnse 418表示网站已经发现你是在爬虫
    response=requests.get(url,headers=header)
```
- 使用BeautifulSoup分析网页
```python
    #需要导入bs4库
    from bs4 import BeautifulSoup as bs
    bs_info = bs(response.text, 'html.parser')  
    # html.parser自带的语法分析器，
    # lxml是第三方的，速度是最快兼容性也比html.parser强
    # 如果不指定则默认使用html.parser
```

- bs_info可以使用findall(),find()
>>>  <font size='2'> 搜索符合条件的标签，只取第一个    bs_info.find('标签',attrs={属性})
 </font>
 >>>  <font size='2'> 匹配所有符合条件的   bs_info.find_all('标签',attrs={属性})
 </font>