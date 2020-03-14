
# ------------------------------------------------
# 使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求，
# 对 http://httpbin.org/post 进行 POST 方式请求，
# 并将请求结果转换为 JSON 格式（转换 JSON 的库和方式不限）。
#----------------------------------------------
import requests
import lxml.etree
import json

url = 'http://httpbin.org/get'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {}
header['user-agent']=user_agent

response = requests.get(url,headers=header)

print("-------------- Print raw rsp headers ----------------")
print(response.headers)
print("-------------- Writing as  JSON format --------------------")#
with open('data.json','w') as f:
    json.dump(response.headers,f)
    
