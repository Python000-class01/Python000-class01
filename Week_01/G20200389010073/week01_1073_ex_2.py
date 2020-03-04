import requests
from datetime import datetime


def get_url_info(str_url, str_mode="get"):
    """ 获取网页信息 """
    if str_mode == "get":
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
        header = {}
        header['user-agent'] = user_agent
        response = requests.get(str_url + 'get', headers=header, timeout=2)
    else:
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        header = {}
        header['user-agent'] = user_agent
        response = requests.post(str_url + 'post', headers=header, timeout=2)
    if response.content:
        print(response.json())


from time import sleep

url = 'http://httpbin.org/'

if __name__ == '__main__':
    time_start_get = datetime.now()
    print(f'>>>> 获取开始 >>>>\n')
    get_url_info(url, 'get')
    print(f'>>>> Get_Json 获取完成 >>>>\n')
    time_using = float((datetime.now() - time_start_get).total_seconds())
    print(f'Get 方式用时s：{time_using}')
    # sleep(1)
    time_start_post = datetime.now()

    get_url_info(url, 'post')
    print(f'>>>> Post_Json 获取完成 >>>>\n')
    time_using = float((datetime.now() - time_start_get).total_seconds())
    print(f'Post 方式用时s：{time_using}')
