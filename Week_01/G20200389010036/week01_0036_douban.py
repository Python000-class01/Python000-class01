import lxml.etree
import requests
import time
import csv


def get_boook(url):
	user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
	header = {}
	header['user-agent'] = user_agent
	response = requests.get(url+'comments/', headers=header)
	selector = lxml.etree.HTML(response.text)

  # //*[@id="comments"]/ul/li[1]/div[2]/p/span
	# contents = selector.xpath('//*[@class="comment-list hot show"]//*[@class="short"]/text()')
	contents = selector.xpath('//*[@class="short"]/text()')
	return contents[:5]


def get_url(url):
	user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
	header = {}
	header['user-agent'] = user_agent
	response = requests.get(url, headers=header)
	selector = lxml.etree.HTML(response.text)

	titles = selector.xpath('//*[@class="pl2"]/a/@title')
	scores = selector.xpath('//*[@class="pl2"]/a/@title')
	num_comments = selector.xpath('//*[@class="star clearfix"]/span[2]/text()')

	url_books = selector.xpath('//*[@class="pl2"]/a/@href')

	detail = []
	for i in range(25):
		time.sleep(3)
		print(f'******爬取第{i}本书籍热评')
		comment_list = get_boook(url_books[i])
		a = {'title': titles[i], 'score': scores[i], 'number reviews': num_comments[i].strip("()\n "), 'comment list hot': comment_list}
		detail.append(a)
	return detail


if __name__ == '__main__':

	urls = tuple(f'https://book.douban.com/top250?start={page * 25}' for page in range(10))
	detail = []

	for page in urls:
		detail += get_url(page)
		time.sleep(5)

	headers = ['title', 'score', 'number reviews', 'comment list hot']
	with open('topbook.csv', 'w', newline='') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=headers)
		writer.writeheader()
		writer.writerows(detail)


# url = 'https://book.douban.com/subject/1007305/'
# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
# header = {}
# header['user-agent'] = user_agent
# response = requests.get(url, headers=header)
# selector = lxml.etree.HTML(response.text)


# titles = selector.xpath('//*[@class="pl2"]/a/text()')
# print(titles[0].strip())

# scores = selector.xpath('//*[@class="star clearfix"]/span[2]/text()')
# print(scores[0])

# Comments = selector.xpath('//*[@class="star clearfix"]/span[3]/text()')
# print(Comments[0].strip("()\n "))

# url_book = selector.xpath('//*[@class="pl2"]/a/@href')
# print(url_book)

# contents = selector.xpath('//*[@class="comment-list hot show"]//*[@class="short"]/text()')
# print(contents)
