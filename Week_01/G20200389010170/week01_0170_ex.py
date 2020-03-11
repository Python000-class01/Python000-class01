import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


URL = "https://movie.douban.com/top250"

def get_top_movies():
    # header
    user_agent = "Mozilla / 5.0(X11;Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome / 80.0.3987.132 Safari / 537.36"

    movie_list = []
    movie_rate = []
    num_rate = []
    comments = []
    headers = {"User-Agent": user_agent}

    for i in range(10):
        cur_url = URL + '?start=' + str(i * 25)
        r = requests.get(cur_url, headers=headers)
        print(r.status_code)

        soup = BeautifulSoup(r.text, "lxml")
        movie_titles = soup.find_all('div', class_='hd')
        movie_comment_data = soup.find_all('div', class_='star')

        for t in movie_titles:
            sub_comments = []
            title_string = t.a.span.text.strip()
            movie_list.append(title_string)

            sub_link = t.a.get('href')
            movie_detail = requests.get(sub_link, headers=headers)
            sub_soup = BeautifulSoup(movie_detail.text, 'lxml')
            short_comments = sub_soup.find_all('span', class_='short')
            for sc in short_comments:
                c = sc.text
                if c is not None:
                    sub_comments.append(c)
            comments.append(sub_comments[1:])

        for comment_data in movie_comment_data:
            rating_data = comment_data("span")
            movie_rate.append(rating_data[1].get_text())
            num_rate.append(str(rating_data[-1].get_text()[:-3]))

    return movie_list, movie_rate, num_rate, comments


def movie_to_csv():
    """
    Convert the data into a .csv file.
    :return: None
    """
    movie_list, movie_rate, num_rate, comments = get_top_movies()
    table = {'name': movie_list, 'rate': movie_rate, "rate_number": num_rate, "comments": comments}
    content = pd.DataFrame(data=table)
    content.to_csv('./movies.csv', encoding='utf-8')


def get_post_by_requests():
    user_agent = "Mozilla / 5.0(X11;Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome / 80.0.3987.132 Safari / 537.36"
    headers = {'User-Agent': user_agent}
    url = "http://httpbin.org/get"
    r = requests.get(url, headers)
    get_result = json.dumps(r.text)
    get_result= json.loads(get_result)

    print(get_result)

    post_content = {
        "name": "Ricky",
        "location": "Mars",
    }

    url2 = "http://httpbin.org/post"
    r2 = requests.post(url2, data=post_content)
    post_result = r2.json()
    print(post_result)


def main():
    movie_to_csv()
    get_post_by_requests()

if __name__ == "__main__":
    main()





