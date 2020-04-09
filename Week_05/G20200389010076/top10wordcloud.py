import jieba.analyse
import pandas as pd
from wordcloud import WordCloud,ImageColorGenerator
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

df=pd.read_csv("./doubancomments.csv",usecols=['comment'])
jieba.analyse.set_stop_words("./stopword.txt")

tagsls=[]
for comment in df['comment'].to_list():
    tags=jieba.analyse.extract_tags(sentence=comment,topK=10)
    tagsls.extend(tags)
tag_str=','.join(tagsls)

background_Image=np.array(Image.open("./boy.png"))
img_colors=ImageColorGenerator(background_Image)
wc=WordCloud(mask=background_Image,
             background_color =None,
             mode="RGBA")
wc.generate_from_text(tag_str)
wc.recolor(color_func=img_colors)
wc.to_file("./wboy.png")

plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.show()