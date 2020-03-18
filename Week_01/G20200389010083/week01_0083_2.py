import requests
import json

def get_json(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/78.0.3904.108 Safari/537.36 '
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    response_json = json.loads(response.text)
    print(response_json)

def post_json(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/78.0.3904.108 Safari/537.36 '
    header = {'user-agent': user_agent}
    response = requests.post(url, headers=header)
    response_json = json.loads(response.text)
    print(response_json)

if __name__ == '__main__':
    get_json("http://httpbin.org/get")
    post_json("http://httpbin.org/post")