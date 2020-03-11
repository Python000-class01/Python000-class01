import requests
import json


if __name__ == '__main__':
    response = requests.get('http://httpbin.org/get')
    print(response)
    json_text = json.loads(response.text)
    print(json_text)
    response = requests.post('http://httpbin.org/post', {'a': 1})
    print(response)
    json_text = json.loads(response.text)
    print(json_text)
