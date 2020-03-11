import requests
import json

P_USERAGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
P_GETURL = 'http://httpbin.org/get'
P_POSTURL = 'http://httpbin.org/post'

headers = {'user-agent': P_USERAGENT}

def getJsonResult():
    jsonObj = json.JSONDecoder().decode(getResponse(P_GETURL).text)
    print(jsonObj)
    print(type(jsonObj))
    return jsonObj

def postJsonResult():
    jsonObj = json.JSONDecoder().decode(postResponse(P_POSTURL).text)
    print(jsonObj)
    print(type(jsonObj))
    return jsonObj

# 获取response
def getResponse(url):
    response = requests.get(url, headers=headers, params={"hello":"world"})
    return  response

def postResponse(url):
    json = {
        'info': {'show_env': '2', 'sex': 'nv'},
        'code': 200,
        'a': 'hello', 'b': 'nihao',
        'files' : {'file': ('test.txt', 'hello')},
        'data': [{'name': 'zhangsan', 'id': '123'}, {'name': 'lisi', 'id': '125'}],
        'id': 1900
    }
    response = requests.post(url, headers=headers, json=json)
    return  response

getJsonResult()
postJsonResult()