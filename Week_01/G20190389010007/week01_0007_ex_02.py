import requests
import json

baseurl = "http://httpbin.org/"
get_params= {'name':'Jack','age':30}
post_params= {'name':'Rose','age':31}
reponse_get = requests.get(baseurl+"get",params=get_params)
reponse_post = requests.post(baseurl+"post",params=post_params)
josn_get = reponse_get.json()
josn_post = reponse_post.json()

