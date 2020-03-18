import requests
import json

def get_post():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    header = {}
    header['User-Agent']=user_agent

    url = 'http://httpbin.org/get'
    response = requests.get(url,headers=header)
    json_get = json.loads(response.text)


    data={
        'username':'wwj',
        'password':'1234'
    }
    url_post = 'http://httpbin.org/post'
    res_post = requests.post(url_post,headers=header,data=data)
    print(type(res_post.text))
    json_port = json.loads(res_post.text)

    return (f'return get json ==={json_get}\n return post json =={json_port}')

if __name__ == '__main__':
    print(get_post())
