import requests
import json
url = 'http://httpbin.org/post'
r = requests.post(url,data = {'name':'chang','age':'66'})
#第一种转换方式
r.json()
#第二种
s = r.text
s_json = json.dumps(s)
