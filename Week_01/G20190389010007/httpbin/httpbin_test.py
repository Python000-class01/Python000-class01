import requests
import json

baseurl = "http://httpbin.org/"
get_params= {'name':'Jack','age':30}
post_params= {'name':'Rose','age':31}
reponse_get = requests.get(baseurl+"get",params=get_params)
reponse_post = requests.post(baseurl+"post",params=post_params)

#to dict
josn_get = json.loads(reponse_get.text)

#to dict
josn_post = json.loads(reponse_post.text)
print(reponse_get)
print(type(reponse_get))
print(josn_get)
print(reponse_post)
print(type(reponse_get))
print(josn_post)