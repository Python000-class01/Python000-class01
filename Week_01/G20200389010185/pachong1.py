import requests
from bs4 import BeautifulSoup as bs
import lxml

#伪装user-agent头
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
header = {}
header['user-agent'] = user_agent


#爬取内容
def get_url_name(url):
    response = requests.get(url,headers=header)
    bs_info = bs(response.text,'lxml')

    for tags_a in bs_info('div',attrs={'class': 'info'}):
        m_name = tags_a.find('span',attrs={'class':'title'}).get_text()
        m_mask = tags_a.find('span',attrs={'class':'rating_num'}).get_text()
        m_p_num = tags_a.find_all('span')[-2].get_text()
        m_url = tags_a.find('a').get('href')


        #短评
        pj = requests.get(m_url,headers=header)
        pj_info = bs(pj.text,'lxml')
        m_pj_info = pj_info.find('div',attrs={"class":"tab"})
        print(m_pj_info)
        print("**************************")







if __name__ == '__main__':
#    for i in range(10):
#        page = 'https://movie.douban.com/top250?start=0' + str(i*25)
        get_url_name('https://movie.douban.com/top250?start=0')






