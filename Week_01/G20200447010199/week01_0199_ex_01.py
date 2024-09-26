import requests;
import csv;

urls = tuple(f'https://movie.douban.com/top250?start={page * 25}'for page in range(10))

user_agen = "'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36"
header = {}
header['user-agent'] = user_agen

for url in urls:
    response = requests.get(url, headers=header)
    from bs4 import BeautifulSoup as bs

    bs_info = bs(response.text, 'html.parser')
    ol = bs_info.findAll('ol', attrs={'class': 'grid_view'})
    for ol in bs_info.findAll('ol', attrs={'class': 'grid_view'}):

        for itemdiv in ol.find_all('div', attrs={'class': 'item'}):
            content_list = []
            # 电影名称
            for tags in itemdiv.find_all('img'):
                content_list.append(tags.get('alt').string)
                #print(tags.get('alt') + ',', end='')

            for info in itemdiv.find_all('div', attrs={'class': 'info'}):
                for stardiv in info.find_all('div', attrs={'class': 'star'}):
                    content_list.append(stardiv.find_all('span')[1].text.string)
                    #print(stardiv.find_all('span')[1].text + ',', end='')
                    content_list.append(stardiv.find_all('span')[3].text.string)
                    #print(stardiv.find_all('span')[3].text);

            # 电影url
            for a in itemdiv.find_all('div', attrs={'class': 'pic'}):
                for tags in a.find_all('a'):
                    single_url = tags.get('href')
                    single_response = requests.get(single_url, headers=header)
                    single_info = bs(single_response.text, 'html.parser')
                    for hotdiv in single_info.find_all('div', attrs={'id': 'hot-comments'}):
                        count = 0;
                        for comment_item_div in hotdiv.find_all('div', attrs={'class': 'comment-item'}):
                            if count < 5:
                                for span_hot in comment_item_div.find_all('span', attrs={'class': 'short'}):
                                    #print(count+1, end='')
                                    #print(span_hot.text)
                                    content_list.append(span_hot.text.string)
                                    count += 1;
            #print()

            #with open(r'D:\reptile.csv','w') as f:
                #writer = csv.writer(f)
                #writer.writerows(content_list)
                #print('write done')