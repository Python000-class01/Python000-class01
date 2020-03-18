import requests
import lxml.etree
result = []
def get_url_name(myurl):
  user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
  header = {}
  header['user-agent'] = user_agent
  response = requests.get(myurl, headers = header)
  selector = lxml.etree.HTML(response.text)
  name = selector.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
  star = selector.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()')
  content = selector.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[4]/text()')
  url = selector.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/@href')
  for net in url:
    responseIntro = requests.get(net, headers = header)
    s = lxml.etree.HTML(responseIntro.text)
    hot = s.xpath('//*[@id="hot-comments"]/div/div/p/span/text()')
  for names,stars,contents in zip(name,star,content):
    for hots in hot:
      result.append([names,stars,contents,hots])
  import pandas
  coulunms_num = ['影片名称','评分','短评数量','热评']
  book1 = pandas.DataFrame(result, columns=coulunms_num)
  book1.to_csv('./book.csv',encoding='utf-8')
  # print(name)
  # print(star)
  # print(content)
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))
from time import sleep
if __name__ == '__main__':
  for page in urls:
    get_url_name(page)
    sleep(5)