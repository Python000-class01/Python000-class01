import requests
import json
from typing import Dict


class Task2:
    get_url = 'http://httpbin.org/get'
    post_url = 'http://httpbin.org/post'

    def get_rq(self) -> dict:
        rp = requests.get(self.get_url)
        return self.to_json(rp)

    def post_rq(self) -> dict:
        some_data = {
            '1': 1,
            '2': 2
        }
        rp = requests.post(self.post_url, data=some_data)
        return self.to_json2(rp.text)

    @staticmethod
    def to_json(rp: requests.Response) -> dict:
        return rp.json()

    @staticmethod
    def to_json2(rp: str) -> dict:
        return json.loads(rp)


task2 = Task2()
print(task2.get_rq())
print(task2.post_rq())
