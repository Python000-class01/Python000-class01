import requests
from bs4 import BeautifulSoup as bs
import xlwt

#代码比较臃肿有时间再优化
filename = '.\douban_book_top250.xlsx'
wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
#创建工作表
sheet = wbk.add_sheet('book Top250', cell_overwrite_ok=True)
sheet.col(0).width = 256 * 30
sheet.col(1).width = 256 * 5
sheet.col(2).width = 256 * 35

#设置表头
th = ['电影名称', '评分', '短评数量', '短评1', '短评2', '短评3', '短评4', '短评5']
for c,each in enumerate(th):
    sheet.write(0, c, each)

excel_tr = 1
# Python 使用 def 定义函数，myurl 是函数的参数
def get_url_name(myurl):
    global excel_tr
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    ##这里如果不去定义 header 为字典直接使用是否会报错？
    header['user-agent'] = user_agent

    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser')



    # Python 中使用 for in 形式的循环,Python 使用缩进来做语句块分隔
    ## 混合使用模块和 for 的功能，因为 tags atag 对象既能支持 find_all 又拥有迭代功能
    star_tr = excel_tr
    for trs in bs_info.find_all('tr', attrs={'class': 'item'}):
        title_tag = trs.find('div', attrs={'class': 'pl2'})
        star_tag = trs.find('span', attrs={'class': 'rating_nums'})
        book_info_link = str(title_tag.a.get('href')) + 'comments/'
        print(book_info_link)
        sheet.write(excel_tr, 0, title_tag.a.get('title'))
        sheet.write(excel_tr, 1, star_tag.get_text())

        # 进去短评页
        brief_comment_response = requests.get(book_info_link,headers=header)
        brief_comment_page = bs(brief_comment_response.text, 'html.parser')
        # 获取短评总数
        total_comments_tag = brief_comment_page.find('span', attrs={'id': 'total-comments'})
        sheet.write(excel_tr, 2, total_comments_tag.get_text())
        # 获取前五短评
        brief_comments_li_tag = brief_comment_page.find_all('li', attrs={'class': 'comment-item'})
        for num in range(5):
            brief_comments_tag = brief_comments_li_tag[num].find('span', attrs={'class': 'short'})
            sheet_col = num + 3
            print(sheet_col)
            sheet.write(excel_tr, sheet_col, brief_comments_tag.get_text())

        sleep(2)
        excel_tr += 1


urls = tuple(f'https://book.douban.com/top250?start={ page * 25}' for page in range(10))
## 推导式功能, 相当于
## for page in range(10)：
##     astring = 'https://book.douban.com/top250?start={ page * 25}'
##     urls = tuple(astring)

from time import sleep
## autopep8 或者其他 IDE 会自动调整 import from 到文件最开头，
## 但是有的时候我们希望在某些对象实例化以后再去进行导入，
## 所以自动移动代码位置不一定每次都是正确的


## 单独执行 python 文件的一般入口
if __name__ == '__main__':
    for page in urls:
        get_url_name(page)
        sleep(5)
    wbk.save(filename)
