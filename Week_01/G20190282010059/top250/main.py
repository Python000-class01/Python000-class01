from top250.request_data import request_list
from bs4 import BeautifulSoup as bs
from top250.bs_info_process import bs_info_process
from top250.data_to_csv import data_to_csv

url = 'https://book.douban.com/top250?start=0'

response = request_list(0)
bs_info = bs(response.text, 'html.parser')
movies = bs_info_process(bs_info)
data_to_csv(movies)

