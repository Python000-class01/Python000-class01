from selenium import webdriver

url = 'https://search.douban.com/movie/subject_search?search_text=你的名字&cat=1002'

browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(10)
href = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[1]/a').get_attribute('href')

print(f'href = {href}')