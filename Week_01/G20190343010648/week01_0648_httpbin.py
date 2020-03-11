import requests
import json


def http_bin_get():
    params = {'key1': '123', 'key2': '456'}
    r = requests.get("http://httpbin.org/get", params=params)
    json_content = json.loads(r.text)
    print(json_content)


def http_bin_post():
    params = {'key1': '123', 'key2': '456'}
    r = requests.post("http://httpbin.org/post", data=params)
    json_content = json.loads(r.text)
    print(json_content)

if __name__ == '__main__':
    http_bin_get()
    http_bin_post()