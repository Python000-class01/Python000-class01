import requests
import json


def request_test():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

    url_get = 'http://httpbin.org/get'
    response_get = requests.get(url_get, headers=headers)
    get_result = json.loads(response_get.text)

    data={
        'username':'andrea',
        'password':'andrea'
    }
    url_post = 'http://httpbin.org/post'
    response_post = requests.post(url_post, headers=headers, data=data)
    post_result = json.loads(response_post.text)

    return (f'GET result:\n{get_result}\n\nPOST result:\n{post_result}')


if __name__ == '__main__':
    print(request_test())
