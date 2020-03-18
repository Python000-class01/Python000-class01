import requests
import json

url_get = "http://httpbin.org/get"
url_post = "http://httpbin.org/post"

def response_by_get(url):
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data


def response_by_post(url, params=None, data=None):
    response = requests.post(url, params=params, data=data)
    print(response.text)
    json_data = json.loads(response.text)
    return json_data


if __name__ == "__main__":
    get_json_data = response_by_get(url_get)
    print(json.dumps(get_json_data, indent=4))
    post_json_data = response_by_post(url_post, params={"Test": "test1", "Python": "3.7"},
                                      data={"name": "xxxx", "avatar": 3})
    print(json.dumps(post_json_data, indent=4))