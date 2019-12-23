# -*- encoding: utf-8 -*-
"""
    @Time   : 2019/8/16 11:41
    @File   : xpath_photo.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task   :爬取指定网页图片
"""
from lxml import etree
import urllib.request, time
class OuMeiSpider(object):
    def __init__(self,start_page,end_page):
        self.start_page = start_page
        self.end_page = end_page
        self.first_url = 'http://sc.chinaz.com/tag_tupian/OuMeiMeiNv.html'
        self.url = 'http://sc.chinaz.com/tag_tupian/OuMeiMeiNv_{}.html'

    def gethtml(self,page):
        if page == 1:
            url = self.first_url
        else:
            url = self.url.format(page)
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        request = urllib.request.Request(url, headers=header)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        return html

    def parse_content(self,content):
        # 生成tree对象
        tree = etree.HTML(content)
        img_src = tree.xpath('//div[@id = "container"]/div/div/a/img/@src2')
        print(len(img_src))

    def run(self):
        for page in range(self.start_page, self.end_page + 1):

            # 拼接地址

            content = self.gethtml(page)
            self.parse_content(content)
            time.sleep(5)











def main():
    start_page = int(input('请输入开始页码:\n'))
    end_page = int(input('请输入终止页码：\n'))
    obj = OuMeiSpider(start_page, end_page)
    # obj = OuMeiSpider(2,8)
    obj.run()

if __name__ == '__main__':
    main()