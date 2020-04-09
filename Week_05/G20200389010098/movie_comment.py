import requests
import lxml.etree
from time import sleep,strptime,mktime
from fake_useragent import UserAgent
import os
import hashlib
import random
import re
import time
import model_comment as mc
from snownlp import SnowNLP
import json
import js2py


class Douban():
    def __init__(self, sub_id, type="movie"):
        self.sub_id=str(sub_id)
        self.statUrl()
    #链接转key
    def md5_convert(self, string):
        m = hashlib.md5()
        m.update(string.encode())
        return m.hexdigest()
    # 统一http请求
    def getHttp(self,url):
        # 缓存文件夹，多线程同时访问时可能都判断到不存在，并尝试创建
        dir = "cache"
        global dirExist
        if not dirExist:
            if not os.path.exists(dir):
                os.makedirs(dir)
            dirExist = True

        url_md5 = self.md5_convert(url)
        key = dir + "/" + url_md5

        if not os.path.exists(key):
            sleep(random.randint(2,5))
            #ua = UserAgent()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
            }
            # print(ua.random)
            res = requests.get(url, headers=headers)
            res.encoding = 'utf-8'
            if (res.status_code == 200):
                with open(key, "w+", newline='', encoding='utf-8-sig') as f:
                    f.write(res.text)
                    print(f"写入缓存{url}")
                    return res.text
                    #return bs(res.text, 'lxml')
            else:
                print(url)
                print(res.status_code)
                print("error")
                exit()
                return False
        else:
            with open(key, encoding='utf-8-sig') as html:
                print(f"读取缓存{url}")
                return html.read()
    def statUrl(self):

        rs=mc.Allreviews()
        for i in rs:

            restext = self.getHttp(
                'https://movie.douban.com/review/'+str(i[0])+'/?start=0#comments' )
            #print(restext)

            asd=restext.split('<div id="comments" class="comment-list"></div>')
            asd = asd[1].split('</div>')

            asd = asd[0].split('<script type="text/javascript">')
            asd = asd[1].split('</script>')
            asd = re.sub(r'\s+', '', asd[0])
            asd = asd.split('var_COMMENTS_CONFIG=')
            asd=asd[1]
            asd = asd.split("'comments':")
            asd = asd[1].split(",'total")
            asd=asd[0]
            comments = json.loads(asd, strict=False)
            for cm in comments:
                text=re.sub(r'\s+', '', cm['text'])
                print(text)
                s2 = SnowNLP(text)
                print(s2.sentiments)
                items={"rid":int(i[0]),"sub_id":int(self.sub_id),"cid":int(cm['id']),"comment":cm['text'],"score1":s2.sentiments}
                mc.Cinsert(items)
            #exit()
    def save(self):
        pass


if __name__ == '__main__':
    dirExist = False
    Douban(1432146)
