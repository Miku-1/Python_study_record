# -*- encoding: utf-8 -*-
"""
@Time    : 2019/8/15 14:29
@File    : bs4_爬虫.py
@Author  : huanyue
@Email   : ******@gmail.com
@IDE     : PyCharm
"""
from bs4 import BeautifulSoup

# 生成对象
soup = BeautifulSoup(open('soup_text.html',encoding= 'utf-8'),'lxml')
# ret = soup.a
# print(ret.attrs)
# print(ret.attrs['href'])
# print(ret['href'])
# print(ret.string)

# ret = soup.div
# print(ret)
# print(ret.text)
# print(ret.text.replace('\n',''))
# print(ret.get_text())

# ret = soup.find('a',class_='juyi')
# ret = soup.find('a',id = 'mu')

# odiv = soup.find('div',class_ ='tang')
# print(odiv)

# ret = soup.find_all('a',limit=2)
# print(ret)

# ret = soup.select('#mu')
# print(ret)



