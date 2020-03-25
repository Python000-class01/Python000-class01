import requests

myurl_1="http://httpbin.org/get"
myurl_2="http://httpbin.org/post"
post_data={'hello':'homework'}
if __name__ == '__main__':
    response=requests.get(myurl_1)
    print(response.json())
    response=requests.post(myurl_2,post_data)
    print(response.json())
