import  requests

url_get = 'https://httpbin.org/get'
url_post = 'https://httpbin.org/post'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'
header = {}
header['user-agent'] = user_agent

response = requests.get(url_get, headers=header)
print(response.json())

response_post = requests.post(url_post)
print(response_post.json())