# -*- encoding: utf-8 -*-
"""
    @Time   : 2019/8/16 10:34
    @File   : xpath_爬虫.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
from lxml import etree
import urllib.request, time, urllib.parse, string

# 本地导入
tree = etree.parse('E:/Python/Pycharm/作业/爬虫/pachong/text.html')
print(tree.xpath('//div'))
# 网络导入
def geturl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    request = urllib.request.Request(url,headers = headers)
    page = urllib.request.urlopen(request)
    html = page.read().decode('utf-8')
    return html






















