from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get('http://www.rrys2019.com/resource/33701')
liulan = driver.find_element_by_xpath('//*[@id="resource_views"]').text
print(liulan)