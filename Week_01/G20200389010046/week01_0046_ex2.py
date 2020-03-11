import requests
import json

#prepare for the header info
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
headers = {}
headers['user-agent'] = user_agent


#test GET
geturl = 'http://httpbin.org/get'
getresponse = requests.get(geturl,headers=headers).text
getresult = json.dumps('get response is %s' % getresponse)
print(getresult)


#test POST
posturl = 'http://httpbin.org/post'
postresponse = requests.post(geturl,data={}, headers=headers).text
postresult = json.dumps('post response is %s' % postresponse)
print(postresult)