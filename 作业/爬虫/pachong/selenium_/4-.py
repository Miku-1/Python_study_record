# -*- encoding: utf-8 -*-
"""
    @Time   : 2019/8/18 11:44
    @File   : 4-.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
from selenium import webdriver

import time

from selenium.webdriver.chrome.options import Options

chrome_options =Options()

chrome_options.add_argument('--headless')

chrome_options.add_argument('--disable-gpu')

path =r'E:\Python\Pycharm\作业\爬虫\pachong\selenium_\chromedriver.exe'

browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)

url = 'http://www.baidu.com'
browser.get(url)
time.sleep(3)
browser.save_screenshot('./photo/baidu.jpg')
browser,quit()