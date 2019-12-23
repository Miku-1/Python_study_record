# -*- encoding: utf-8 -*-
"""
    @Time   : 2019/8/18 14:56
    @File   : 6--.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
import requests

# url = 'https://cn.bing.com/ttranslatev3?isVertical=1&&IG=BE3B0A4E96604F089DB9CBDCBFB31063&IID=translator.5028.2'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
        }
# data ={
#     'client':'webapp',
#     'sl': 'zh-CN',
#     'tk': '301672.145726',
#     'q': '小明'
# }
# r = requests.get(url = url,params=data,headers = headers)
# print(r.url)
import requests

url = 'https://cn.bing.com/ttranslatev3?isVertical=1&&IG=BE3B0A4E96604F089DB9CBDCBFB31063&IID=translator.5028.2'

def translate_weiruan(info,fr='zh-CHS',to="en"):
    print('翻译结果：'+requests.post(url,data={'text':info,'from':fr,'to':to,'doctype':'json'}).json()['translationResponse'])

def is_Chinese(str):  #判断输入的内容是否是中文
    for ch in str:
        if '\u4e00' <= ch <= '\u9fff':
            return True
        else:
            return False

def start_translate():
    trans = input('翻译内容：')
    if is_Chinese(trans):   #实现自动判断，中英互译
        translate_weiruan(trans)
    else:
        translate_weiruan(trans,fr='en',to='zh-CHS')

if __name__ == '__main__':
    print('          翻译结果由微软翻译提供！（请确保网络已连接）')
    while True:
        start_translate()
        print('\n')
