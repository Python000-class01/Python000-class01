import requests

url = "http://httpbin.org/get"
url2 = "http://httpbin.org/post"

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"

header = {'user-agent': user_agent}

#get请求
def get (url):
    r = requests.get(url,headers = header)
    return r.json()

#post请求
def post (url):
    r = requests.post(url,headers = header)
    return r.json()

if __name__ == '__main__':
     print("get",get(url))
     print("post",post(url2))
