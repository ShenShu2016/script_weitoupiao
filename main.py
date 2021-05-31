from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

wd=webdriver.Chrome(r'chromedriver.exe')

wd.get('https://www.baidu.com/')

input_=wd.find_element_by_id('kw')

input_.send_keys('shushengacademy')

search_=wd.find_element_by_id('su')

ActionChains(wd).move_to_element(search_).click(search_).perform()

login=wd.find_element_by_class_name('register-btn')
sleep(10)

wd.find_element_by_tag_name('td')
wd.find_element_by_link_text()
wd.find_element_by_tag_name()
wd.implicitly_wait(15)