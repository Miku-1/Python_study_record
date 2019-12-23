# -*- encoding: utf-8 -*-
"""
    @Time   : 2019/8/18 11:11
    @File   : 3-.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task   模拟滚动条的拖动
"""
from selenium import webdriver
from time import sleep

url = 'https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action='
path = r'E:\Python\Pycharm\作业\爬虫\pachong\selenium_\phantomjs-2.1.1-windows\bin\phantomjs.exe'
# 创建对象
browser = webdriver.PhantomJS(path)
browser.get(url)
sleep(3)
# browser.save_screenshot('./photo/豆瓣喜剧.png')
# 模拟滚动条到底部
js = 'document.body.scrollTop = 20000'
# browser.execute_script(js)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(12)
browser.save_screenshot('./photo/1.png')

# 获取执行完js后的网页代码
# browser.page_source
# with open('douban.html','w',encoding='utf8') as f:
#     f.write(browser.page_source)

# from bs4 import BeautifulSoup
# # 生成soup对象
# soup = BeautifulSoup(browser.page_source)
# #
browser.quit()