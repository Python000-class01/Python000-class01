import requests


# request-get請求
def get_url_info(url):
    response = requests.get(url, headers=header)
    result = response.json()
    return result


# request-post請求
def post_url_info(url):
    response = requests.post(url, headers=header, data={'key':'value'})
    result = response.json()
    return result


get_url = 'http://httpbin.org/get'
post_url = 'http://httpbin.org/post'
# user agent
header = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}


if __name__ == '__main__':
    get_result = get_url_info(get_url)
    post_result = post_url_info(post_url)
    print('Get info: ',get_result,'\n',
          'Post info: ',post_result)