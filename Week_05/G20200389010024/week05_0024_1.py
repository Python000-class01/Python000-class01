import requests
from bs4 import BeautifulSoup as bs
import jieba.analyse
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
from snownlp import SnowNLP

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
header = {}
header['user-agent'] = user_agent
bookname = '我不喜欢人类，我想住进森林'

def Bookreview(url):
    response = requests.get(url,headers = header)
    bs_info = bs(response.text,'html.parser')
    bookreview = ''
    for tag in bs_info.find_all('div',attrs={'class':'short-content'}):
        bookreview = bookreview + tag.contents[0]
    return bookreview

web = 'https://book.douban.com/subject/34869425/reviews?start=0'
listall = ''
for page in range(2):
    num = 20*page
    web = 'https://book.douban.com/subject/34869425/reviews?start='+ str(num)
    listone = Bookreview(web)
    listall = listall + listone
    print(listall)

top10keyword = jieba.analyse.extract_tags(listall, topK = 10)
top10keyword_string = ','.join(top10keyword)

wc = WordCloud(
width=600,
height=200,
margin= 2,
ranks_only=None,
prefer_horizontal=0.9,
mask=None,
color_func=None,
max_words=200,
stopwords=None,
random_state=None,
background_color="#ffffff",
font_step=1,
mode="RGB",
regexp= None,
collocations=True,
normalize_plurals= True,
contour_width=0,
colormap="viridis",
contour_color = "Blues",
repeat = False,
scale = 2,
min_font_size= 10,
max_font_size= 200)


wc.generate_from_text(top10keyword_string)

plt.imshow(wc,interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout()

wc.to_file('book.png')

plt.show()

for s in listall:
    s = SnowNLP(listall)
    print(s.sentiments)

