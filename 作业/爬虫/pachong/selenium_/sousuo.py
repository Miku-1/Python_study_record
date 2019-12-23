# -*- encoding: utf-8 -*-
"""
    @Time   : 2019/8/18 17:57
    @File   : sousuo.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
from selenium import webdriver

import time

from selenium.webdriver.chrome.options import Options


path =r'E:\Python\Pycharm\作业\爬虫\pachong\selenium_\chromedriver.exe'

browser = webdriver.Chrome(executable_path=path)

url ='https://www.8684.cn'
browser.get(url)

time.sleep(3)
change_button = browser.find_element_by_id('cnBuscity')
change_button.click()
time.sleep(2)
js = 'document.getElementById(citys).scrollTop=50'
browser.execute_script(js)
xian_button = browser.find_element_by_id('xian')
xian_button.click()

