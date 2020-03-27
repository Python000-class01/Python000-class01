import requests
import json

def get_json(url):
    header={}
    header['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    payload= {'key1': 'value1', 'key2': 'value2'}
    response=requests.get(url,headers=header,params=payload)
    res_dict =json.loads(response.text)
    res_json = json.dumps(res_dict)
    print(res_json)

def post_json(url):
    header={}
    header['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    payload= {'key1': 'value1', 'key2': 'value2'}
    response=requests.post(url,headers=header,data=payload)
    res_dict =json.loads(response.text)
    res_json = json.dumps(res_dict)
    print(res_json)

if __name__=='__main__':
    url_1='http://httpbin.org/get'
    get_json(url_1)
    url_2='http://httpbin.org/post'
    post_json(url_2)