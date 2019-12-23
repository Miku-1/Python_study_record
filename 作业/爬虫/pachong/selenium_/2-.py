# -*- encoding: utf-8 -*-
"""
    @Time   : 2019/8/18 9:57
    @File   : 2-.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
from selenium import webdriver
from time import sleep

url= 'http://www.baidu.com'
path = 'E:\Python\Pycharm\作业\爬虫\pachong\selenium_\chromedriver.exe'
browser = webdriver.Chrome(path)
try:
    # 控制浏览器跳转到这个网页
    browser.get(url)
    # 找到输入框往里面输入内容
    sleep(2)
    input_board = browser.find_element_by_id('kw')
    # 控制按钮进行点击
    input_board.send_keys('动漫')
    # 找到百度一下按钮
    sleep(1)
    search_button = browser.find_element_by_id('su')
    # 点击按钮
    search_button.click()
    sleep(3)

    # 点击a连接
    link1 = browser.find_element_by_xpath('//*[@id="2"]/h3/a')
    link1.click()
    sleep(3)
finally:
    # 关闭当前窗口
    browser.close()
    # 关闭所有标签
    # browser.quit()

# 根据class查找
browser.find_element_by_class_name()
# 根据a连接内容查找
browser.find_element_by_link_text()
browser.find_elements_by_link_text()
browser.find_element_by_name()
browser.find_element_by_xpath()