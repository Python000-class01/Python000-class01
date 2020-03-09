import requests
import json

url = 'http://httpbin.org/get'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3521.2 Safari/537.36',
}

response = requests.get(url, headers=headers)

print(response.json())
