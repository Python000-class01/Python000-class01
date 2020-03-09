import requests
from lxml import etree
import xlwt

#代码比较臃肿有时间再优化
filename = '.\douban_book_top250_xpath.xlsx'
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
    
    header['user-agent'] = user_agent

    response = requests.get(myurl,headers=header)
    bs_info = etree.HTML(response.text)
    
    ## 起始行数
    a_tags = bs_info.xpath('//div[@class="pl2"]/a')

    for a_tag in a_tags:
        sheet.write(excel_tr, 0, a_tag.get('title').strip())
        
        book_info_link = str(a_tag.get('href')) + 'comments/'
        # 进去短评页
        brief_comment_response = requests.get(book_info_link,headers=header)
        brief_comment_info = etree.HTML(brief_comment_response.text)

        # 获取短评总数
        total_comments = brief_comment_info.xpath('//span[@id="total-comments"]/text()')
        sheet.write(excel_tr, 2, total_comments)

        short_comments = brief_comment_info.xpath('//span[@class="short"]/text()')

        for num in range(5):
            sheet_col = num + 3
            sheet.write(excel_tr, sheet_col, short_comments[num])

        sleep(1)
        excel_tr += 1
        

    excel_tr = excel_tr - 25
    scores = bs_info.xpath('//span[@class="rating_nums"]/text()')
    for score in scores:
        sheet.write(excel_tr, 1, score.strip())
        excel_tr += 1

urls = tuple(f'https://book.douban.com/top250?start={ page * 25}' for page in range(10))

from time import sleep

## 单独执行 python 文件的一般入口
if __name__ == '__main__':
    for page in urls:
        get_url_name(page)
        sleep(5)
    wbk.save(filename)

