import requests
import json
from pprint import pprint


def get_response(url):
    user_agent = user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header["user-agent"] = user_agent
    response = requests.get(url + "get", headers=header)
    print("GET response:")
    pprint(response.json())

    response = requests.post(
        url + 'post', data={'key': 'value'}, headers=header)
    print("\n\nPOST response:")
    pprint(response.json())


def main():
    url = "http://httpbin.org/"
    get_response(url)


if __name__ == "__main__":
    main()
