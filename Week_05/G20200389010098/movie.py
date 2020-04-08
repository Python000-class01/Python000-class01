import requests
import lxml.etree
from time import sleep,strptime,mktime
from fake_useragent import UserAgent
import os
import hashlib
import random
import re
from model_comment import Rinsert
import json


class Douban():
    def __init__(self, sub_id, type="movie"):
        self.sub_id=str(sub_id)
        self.type = type
        self.pager = 20
        self.sum = 0
        self.offest = 0
        self.rate = ['很差','较差','还行','推荐','力荐']
        # Rinsert({"cid":1,"sub_id":1,"star":1,"comment":"123123123","info_time":1})
        # exit()
        self.statUrl()
    def toStamp(self, string):
        timeArray = strptime(string, "%Y-%m-%d %H:%M:%S")
        return int(mktime(timeArray))
    def getRate(self, list):
        if(len(list)<=0):
            return 0
        if (list[0] in self.rate):
            return self.rate.index(list[0])+1
        else:
            return 0

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
            ua = UserAgent()
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
        restext=self.getHttp('https://movie.douban.com/subject/'+self.sub_id+'/reviews?start='+str(self.offest))
        selector = lxml.etree.HTML(restext)
        sum = selector.xpath('//*[@class="count"]/text()')[0]
        self.sum=int(sum[2:-2])
        self.getReview(restext=restext)
        self.offest+=20
        while (self.offest <= self.sum):
            self.getReview()
            self.offest += 20

    def getReview(self,restext=None):
        if(restext is None):
            restext = self.getHttp('https://movie.douban.com/subject/'+self.sub_id+'/reviews?start='+str(self.offest))
        selector = lxml.etree.HTML(restext)
        rid = selector.xpath('//*[@class="review-short"]//@data-rid')

        if(len(rid)>0):
            #comments = [re.sub(r'\s+', '', x) for x in selector.xpath('//*[@class="short"]/text()')]
            #star = [self.getRate(x) for x in selector.xpath('//*[@class="main-hd"]/span[1]/@title')]
            star = selector.xpath('//*[@class="main-hd"]/span[1]')
            info_time =[self.toStamp(x) for x in selector.xpath('//*[@class="main-meta"]/text()')]
            for i, v in enumerate(rid):


                ss=self.getRate(star[i].xpath('@title'))
                full = self.getHttp('https://movie.douban.com/j/review/'+str(v)+'/full')
                if(full is not False):
                    rs=json.loads(full)
                dr = re.compile(r'<[^>]+>', re.S)
                review = dr.sub('', rs['html'])
                review=re.sub(r'\s+', '', review)
                review = re.sub(r'&nbsp;', '', review)


                items={"rid":int(v),"sub_id":int(self.sub_id),"star":int(ss),"review":review,"info_time":int(info_time[i])}
                # print(items)
                # exit()
                Rinsert(items)
        #exit()




    def save(self):
        pass


if __name__ == '__main__':
    dirExist = False
    Douban(1432146)
