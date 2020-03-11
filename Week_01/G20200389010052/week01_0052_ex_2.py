import requests


def json_test():
    """
    使用 requests 库对 http://httpbin.org/ 分别用 get 和 post 方式访问，并将返回信息转换为 JSON
    """
    response_get = requests.get('http://httpbin.org/get')
    response_post = requests.post('http://httpbin.org/post', data={'k': 'v'})
    print(response_get.json())
    print(response_post.json())


if __name__ == '__main__':
    json_test()