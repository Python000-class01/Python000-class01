import requests as re
import pandas as pd
# get与post
def _get_(url):
    r=re.get(url,params=name)
    r.json()
    return r.json()
    # print(r.json())
def _post_(url):
    r=re.post(url,data=name)
    r.json()
    return r.json()
    # print(r.json())
def _panda_post_(st,url):
    _post_(url)
    columns=[st]
    content=[str( _post_(url))]
    DATA=pd.DataFrame(columns=columns,data=content)
    DATA.to_csv(st +'.csv',encoding='utf-8')
def _panda_get_(st,url):
    _get_(url)
    columns=[st]
    content=[str(_get_(url))]
    DATA=pd.DataFrame(columns=columns,data=content)
    DATA.to_csv(st +'.csv',encoding='utf-8')


if __name__ =='__main__':
    name = {'name': 'shuai', 'password': '123abc'}
    url1=' http://httpbin.org/get'
    url2='http://httpbin.org/post'
    _panda_get_('get',url1)
    _panda_post_('post',url2)


