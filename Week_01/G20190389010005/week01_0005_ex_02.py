import requests
import json


# get请求，并转成 json
def parse_get():
    url = 'http://httpbin.org/get'
    params = data = {'name': '大中国', 'password': '123'}
    response = requests.get(url,  params=params, headers=headers)
    data = response.text
    print(data)

    # 转json
    data_json = json.loads(data, encoding='UTF-8')
    print(type(data_json))


# post 请求并转成 json
def parse_post():
    data = {'name': 'tony', 'password': '123'}
    response = requests.post('http://httpbin.org/post',
                             data=json.dumps(data),
                             headers={'Content-Type': 'application/json'})
    data = response.text
    print(data)

    # 转json
    data_json = json.loads(data, encoding='UTF-8')
    print(type(data_json))


if __name__ == '__main__':
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 ' \
                 'Safari/537.36'
    headers = {
        "User-Agent": user_agent
    }

    parse_get()

    parse_post()
