import requests

respone = requests.get("http://httpbin.org/get");
print(f"get:",respone.json())

respone1 = requests.post("http://httpbin.org/post")
print(f"post:",respone1.json())
