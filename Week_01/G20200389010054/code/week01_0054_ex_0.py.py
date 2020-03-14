# 要求:
# 安装并使用 requests、bs4 库，
# 爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，
# 并以 UTF-8 字符集保存到 csv 格式的文件中。
import requests
from bs4 import BeautifulSoup as bs
import csv
from time import sleep

with open('movie.csv','a',encoding='utf-8',newline='') as myFile:
    myWriter = csv.writer(myFile)
    myFile.seek(0)
    myFile.truncate()
    myWriter.writerow(["电影名","评分","评论人数","热评1","热评2","热评3","热评4","热评5"])
        
# Python 使用def定义函数，myurl是函数的参数
def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(myurl,headers=header)
    print(response)
    bs_info = bs(response.text, 'html.parser')
    
    # 获取一页中的每部电影信息
    for tags in bs_info.find_all('div',attrs={'class':'info'}):
        # 分别获取电影名,评分,评论人数
        title = tags.find('span',attrs={'class':"title"}).text      
        grade = tags.find('span',attrs={'class':'rating_num'}).text
        pep_num = tags.find('div',attrs={'class':'star'}).contents[7].text
        # 获取前五的短评
        http = str(tags.find('a')['href'])
        res= requests.get(http,headers = header)
        page = bs(res.text,'html.parser')
        c_comment = []
        for comments in page.find_all('div',class_='comment'):
            comment = comments.find('span',attrs={'class':'short'}).text          
            # print(comment)
            c_comment.append(comment)

        #获取
        with open('movie.csv','a',encoding='utf-8',newline='') as myFile:
            myWriter = csv.writer(myFile)   
            #防止列表元素溢出  
            try:       
                myWriter.writerow([title,grade,pep_num,c_comment[0],c_comment[1],c_comment[2],c_comment[3],c_comment[4]])
            except:
                continue
        sleep(1)
        # print("ok")

# 生成包含所有页面的元组
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))

if __name__ == '__main__':
    for page in urls:
        get_url_name(page)
        sleep(1)