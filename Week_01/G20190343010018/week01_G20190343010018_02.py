import requests

url1 = "http://httpbin.org/get"
url2 = "http://httpbin.org/post"

def get (url):
    r = requests.get(url1)
    return r.json()

def post (url):
    r = requests.post(url)
    return r.json()

if __name__ == '__main__':
    print(get(url1))
    print(post(url2))