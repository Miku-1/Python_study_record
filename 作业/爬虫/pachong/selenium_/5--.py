# -*- encoding: utf-8 -*-
"""
    @Time   : 2019/8/18 14:21
    @File   : 5--.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
import requests
# url = 'https://www.8684.cn'
url = 'https://www.baidu.com/s?'
data = {
    'ie':'utf-8',
    'wd':'美女'
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
        }
#
# # 发送请求
# r = requests.get(url=url,params=data,headers=headers)
# print(r.text)
# with open('123.html','w',encoding='utf8')as f:
#     f.write(r.text)

# 使用代理
# proxy = {
#     'http':'ip + : + 端口'
# }
# r = requests.get(url = url, headers = headers, proxies = proxy)