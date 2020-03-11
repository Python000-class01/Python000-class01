import requests	
from bs4 import BeautifulSoup as bs
		
        
# Python 使用 def 定义函数，myurl 是函数的参数
	
def get_url_name(myurl):	
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'	
    header = {}
	
    ##这里如果不去定义 header 为字典直接使用是否会报错？	
    header['user-agent'] = user_agent	 	
    response = requests.get(myurl,headers=header)	
    bs_info = bs(response.text, 'html.parser')
	
 
	
    # Python 中使用 for in 形式的循环,Python 使用缩进来做语句块分隔	
    ## 混合使用模块和 for 的功能，因为 tags atag 对象既能支持 find_all 又拥有迭代功能
	
    for tags in bs_info.find_all(attrs={'class':'info'}):
    #print(tags)

        for atag in tags.find_all('a',):
            print(atag.get('href'))
        
        for atag in tags.find_all('span',):
            print(atag.get_text('title'))

    
	
        
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}' for page in range(10))
	
## 推导式功能, 相当于	
## for page in range(10)：	
##     astring = 'https://book.douban.com/top250?start={ page * 25}'	
##     urls = tuple(astring)
	 	 	
from time import sleep
	
## autopep8 或者其他 IDE 会自动调整 import from 到文件最开头，	
## 但是有的时候我们希望在某些对象实例化以后再去进行导入，	
## 所以自动移动代码位置不一定每次都是正确的
	 
	
## 单独执行 python 文件的一般入口
	
if __name__ == '__main__':	
    for page in urls:	
        get_url_name(page)	
        sleep(5)



