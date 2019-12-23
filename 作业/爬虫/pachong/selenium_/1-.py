# -*- encoding: utf-8 -*-
"""
    @Time   : 2019/8/18 9:18
    @File   : 1-.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
from selenium import webdriver
from time import sleep

path = r'E:\Python\Pycharm\作业\爬虫\pachong\selenium_\phantomjs-2.1.1-windows\bin\phantomjs.exe'
# 创建浏览器对象
browser = webdriver.PhantomJS(path)
url = 'http://www.baidu.com'
#
browser.get(url)
sleep(3)
# 拍照片记录状态
# browser.save_screenshot('./photo/baidu.png')
# 打开搜索栏,并输入'娘炮'
input_bar = browser.find_element_by_id('kw').send_keys('娘炮')
sleep(2)
# 点击'百度一下'按钮
search_button = browser.find_element_by_id('su').click()
sleep(3)
# 将搜索结果截图保存
browser.save_screenshot('./photo/娘炮.jpg')
sleep(1)
# 退出
browser.quit()