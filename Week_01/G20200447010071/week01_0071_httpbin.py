import requests


# GET请求
def get():
    try:
        url = 'http://httpbin.org/get'
        json = requests.get(url).json()
        print(json)
    except Exception as e:
        print(e)


# POST请求
def post():
    try:
        url = 'http://httpbin.org/post'
        data = {
            'data1': 'test'
        }
        json = requests.post(url, data=data).json()
        print(json)
    except Exception as e:
        print(e)


get()
post()
