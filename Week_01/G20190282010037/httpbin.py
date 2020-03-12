# Python 训练营 第一周作业 第二部分 20200304 00:36 @纪如军
import requests

def get_url(url):

    #Get 访问并返回JSON
    response_get = requests.get(url+'get')
    print(response_get.json())

    #Post 访问并返回JSON
    response_post = requests.post(url+'post')
    print(response_post.json())



url =  'http://httpbin.org/'

#程序主入口
if __name__ == '__main__':
        get_url(url)