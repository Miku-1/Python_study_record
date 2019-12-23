# -*- encoding: utf-8 -*-
"""
    @Time   : 2019/8/17 23:39
    @File   : jingdong.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
from selenium import webdriver
from time import sleep
import csv

path = 'E:\Python\Pycharm\作业\爬虫\pachong\selenium_\chromedriver.exe'
browser = webdriver.Chrome(path)
try:
    # 控制浏览器跳转到这个网页
    browser.get('https://item.jd.com/100002795959.html#none')
    button = browser.find_element_by_xpath("//li[@clstag='shangpin|keycount|product|shangpinpingjia_1']")  # 获取商品评论按钮
    # 控制按钮进行点击
    button.click()
    # 等待网页加载，防止网页加载过慢
    sleep(10)
    # 新建并打开comment_con.csv文件
    with open('comment_con.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['user_name', 'comment'])
        for n in range(99):  # 进行99次循环
            m = n + 1
            print(m)
            user = browser.find_elements_by_xpath("//div[@class='user-info']")  # 获取用户名
            lis = browser.find_elements_by_xpath("//p[@class='comment-con']")  # 获取评论
            for i in range(len(user)):
                writer.writerow([user[i].text, lis[i].text])
#             button2 = browser.find_element_by_class_name("ui-pager-next")  # 获取下一页按钮
#             print(button2.text)
#             sleep(1)
#             print("第%d页" % m)
#             button2.click()
#             sleep(5)
finally:
    browser.quit()  # 关闭所有窗口
    browser.close()  # 关闭当前窗口