import requests
import lxml.etree

from time import sleep


movie_info = []

urls = tuple \
    (f'https://movie.douban.com/subject/34670218/comments?start={ page * 20 }&limit=20&sort=new_score&status=P' for page in range(10))

# 获取短评数据
def get_url_name(url):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(url, headers=header)
    selector = lxml.etree.HTML(response.text)
    for i in range(21):
        star = selector.xpath(f"//div[@class='comment-item'][{i}]//span[@class='comment-info']/span[2]/@title")
        pingjia = selector.xpath(f"//div[@class='comment-item'][{i}]//div[@class='comment']/p/span/text()")

        movie_info.append(star + pingjia)
        print(movie_info)


 def sentiment_analyais(data):
     column_name = ['star', 'pingjia']
     df = pd.DataFrame(columns=column_name, data=data)
     print(df.head())
     star_to_number = {
         '力荐': 5,
         '推荐': 4,
         '还行': 3,
         '较差': 2,
         '很差': 1
     }
     df['score'] = df['star'].map(star_to_number)
     df = df.dropna(how='any')

     def _sentiment(text):
         s = SnowNLP(text)
         return s.sentiments

     df["sentiment"] = df.shorts.apply(_sentiment)

     # 分析平均值
     print(df.sentiment.mean())

     return df

 def to_sql(df):
     engine = create_engine(
         "mysql+pymysql://root:rootaa@10.142.105.187:3306/pro_sdq")
     con = engine.connect()
     df.to_sql(name='test', con=con, if_exists='append', index=False)

if __name__ == '__main__':
    for page in urls:
        get_url_name(page)
        sleep(10)
    df = sentiment_analyais(movie_info)
    to_sql(df)
