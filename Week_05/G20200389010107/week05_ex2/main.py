import requests
from requests.exceptions import RequestException
import pymysql
import pymysql.cursors
from lxml import etree
import re
import time
import os
from snownlp import SnowNLP


def parse_comment(url, out_handle):
    try:
        headers = headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        page_offset = 1
        has_next_page = True

        while has_next_page is True:
            has_next_page = parse_one_page(url, page_offset, out_handle)
            page_offset += 1
            time.sleep(1)

    except RequestException:
        return None


def parse_one_page(book_url, page_offset, out_handle):

    url = f"{book_url}/comments/hot?p={page_offset}"

    has_next_page = False
    headers = headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

    response = requests.get(url, headers=headers)
    if response.status_code == requests.codes.ok:
        html = etree.HTML(response.text)
        comment_node_list = html.xpath('//li[@class="comment-item"]')
        # comment_text_list = html.xpath(
        #    '//span[@class="short"]/text()')
        # print(comment_text_list)
        for comment_node in comment_node_list:
            comment_text = comment_node.xpath(
                './/span[@class="short"]/text()')[0]
            rating_string_list = comment_node.xpath(
                './/span[contains(@class, "user-stars")]/@class')
            if len(rating_string_list) > 0:
                rating = re.findall(r'\d+', rating_string_list[0])[0]
            else:
                rating = -1
            #print(comment_text, rating)
            comment_text = clean_text(comment_text)
            out_handle.write(f"{rating}, {comment_text}\n")

        page_link_list = html.xpath('//a[@class="page-btn"]/@href')
        for link in page_link_list:
            offset = re.findall(r'\d+', link)[0]
            if int(offset) > page_offset:
                has_next_page = True
                break

    else:
        print(f"parse page {url} failed. status code: {response.status_code}")
        return has_next_page

    return has_next_page


def clean_text(raw_text):
    cleaned_text = raw_text.replace("\n", " ")
    cleaned_text = cleaned_text.replace("\r", " ")
    fil = re.compile(u'[^0-9a-zA-Z\u4e00-\u9fa5.，,。？“”]+', re.UNICODE)
    cleaned_text = fil.sub(' ', cleaned_text)
    return cleaned_text


def analyze_sentiment(csv_path, final_output):
    '''
    connection = pymysql.connect(host='localhost',
                                 user='user',
                                 password='password',
                                 charset='utf8mb4',
                                 )
    mycursor = connection.cursor()
    mycursor.execute("CREATE DATABASE douban_book_DB")
    '''

    with open(csv_path, "r") as f, open(final_output, "w") as w:
        w.write(f"user_rating, NLP_calculated_rating, comment_text\n")
        for line in f.readlines():
            user_rating = line.split(",")[0]
            comment_text = " ".join(line.split(",")[1:])
            user_rating = float(user_rating)/50.0
            s = SnowNLP(clean_text(comment_text))
            #print(user_rating, s.sentiments)
            w.write(f"{user_rating:.2f}, {s.sentiments:.2f}, {comment_text}")


if __name__ == "__main__":
    book_url = "https://book.douban.com/subject/3025921/"
    result_csv_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "parse_result.csv")
    final_output = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "sentiment_analysis_result.csv")

    with open(result_csv_path, "w") as f:
        parse_comment(book_url, f)

    print(f"parsed raw result in {result_csv_path}")
    analyze_sentiment(result_csv_path, final_output)
    print(f"final sentiments result saved to: {final_output}")
