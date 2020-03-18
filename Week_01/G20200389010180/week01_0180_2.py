import requests

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
header = {}
header['user-agent'] = user_agent

url = 'http://httpbin.org/get'
response = requests.get(url, headers=header, timeout=10)
get_json = response.json()
print(f'Get_JSON: \n{get_json}')

url = 'http://httpbin.org/post'
response = requests.post(url, headers=header, timeout=10, data={'key':'value'})
post_json = response.json()
print(f'Post_JSON: \n{post_json}')





