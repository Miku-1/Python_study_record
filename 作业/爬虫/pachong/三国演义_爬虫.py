# -*- encoding: utf-8 -*-
"""
@Time    : 2019/8/15 16:15
@File    : 诗词名句.py
@Author  : huanyue
@Email   : ******@gmail.com
@IDE     : PyCharm
"""
from bs4 import BeautifulSoup
import urllib.request
import time
#
def geturl(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    request = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    return html

def parse_content(content):
    soup = BeautifulSoup(content,'lxml')
    # 根据方法查找所有的章节和内容
    odiv = soup.find('div',class_ = 'book-mulu')
    # print(odiv)
    get_text(odiv)



def get_text(odiv):
    # 生成soup对象
    # soup = BeautifulSoup(odiv, 'lxml')
    #  根据方法查找所有的章节a链接
    oa_list = odiv.find_all('a')
    print(len(oa_list))
    fp = open('三国演义.txt','w',encoding='utf8')
    #  遍历每一个a对象的标题
    for oa in oa_list:
        # 得到标题
        title = oa.string
        # 得到链接
        href = 'http://www.shicimingju.com' + oa['href']
        # print(href)
        # 向href发起请求 解析响应 得到内容
        response = geturl(href)
        # 生成soup
        soup = BeautifulSoup(response, 'lxml')
        # 找到章节内容
        odiv = soup.find('div', class_ = 'chapter_content')
        # 返回内容

        fp.write(title + '\n' + odiv.text)

        time.sleep(1)
    fp.close()







def main():
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    # 构建请求对象,得到响应,
    content = geturl(url)
    # 通过bs4解析网页内容
    parse_content(content)


if __name__ == '__main__':
    main()
