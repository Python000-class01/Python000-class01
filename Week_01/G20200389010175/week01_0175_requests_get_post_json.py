import requests
import json
import ast

root_url = 'http://httpbin.org/'


def get_json(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    header = {'user-agent': user_agent}
    payload = {'key1': 'value1', 'key2': 'value2'}
    response = requests.get(url+'get', headers=header, params=payload).text  # 字符串类型
    # str>dict（字典），使用literal_eval进行转换既不存在使用 json 进行转换的问题，也不存在使用 eval 进行转换的 安全性问题，因此推荐使用 ast.literal_eval。
    res_dict = ast.literal_eval(response)
    res_json = json.dumps(res_dict)  # json格式字符串
    print(res_json)


def post_json(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    header = {'user-agent': user_agent}
    data = {'key1': 'value1', 'key2': 'value2'}
    response = requests.post(url+'post', headers=header, data=data).text  # 字符串类型
    res_dict = json.loads(response)
    res_json = json.dumps(res_dict)  # json格式字符串
    print(res_json)


if __name__ == '__main__':
    get_json(root_url)
    post_json(root_url)
