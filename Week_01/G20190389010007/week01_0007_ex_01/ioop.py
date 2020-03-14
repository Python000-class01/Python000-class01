from movie import Movie
import pandas as pd
from pandas import DataFrame
import sys
import csv
from threading import Thread
from time import sleep
def export_by_data_frame(movies):
    # Movie类里面评论存成了个数组, 写入csv进行分割
    dffinal=DataFrame()
    for movie in movies:
        moviedict=vars(movie)
        dfcomments = DataFrame(moviedict["comment_top5"],columns=['comment'])
        dfmoive_trans=DataFrame(moviedict).join(dfcomments).drop('comment_top5', axis=1)
        dffinal=pd.concat([dffinal,dfmoive_trans])
    return dffinal
    
    #通过pandas写入csv
def append_to_CSV(movies):
    #格式设置为utf_8_sig
    export_by_data_frame(movies).to_csv("movie_data1.csv",encoding="utf_8_sig",index=False,mode="a")

    #通过writer一行一行写入
def append_toCSV_by_writer(movies):
    movie_dict= export_by_data_frame(movies).to_dict(orient="record")
    with open('movie_data.csv', 'w',encoding='utf_8_sig',newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file,['title','rating_num','comment_num','comment'])
        csv_writer.writeheader()
        # csv_writer.writerow(['title','rating_num','comment_num','comment'])
        csv_writer.writerows(movie_dict)






