# -*- encoding: utf-8 -*-
"""
    @Time   : 2019年8月19日 下午4:26
    @File   : 多线程爬虫.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
from  queue import Queue
from threading import Thread,Lock
from time import sleep
import requests
from bs4 import BeautifulSoup

class CrawlThread(Thread):
    def __init__(self,crawl_name,page_queue,data_queue):
        super().__init__()
        self.crawl_name = crawl_name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.url = 'http://www.fanjian.net/jianwen-{}'
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

    def run(self):
        '''
        从页码队列中去一个page
        生成新的url
        发送请求 得到响应数据
        '''
        while 1:
            page = self.page_queue
            url = self.url.format(page)
            r = requests.get(url =url,headers = self.header)
            # 将内容写进数据队列
            self.data_queue.put(r.text)
        print(f'{self.crawl_name}')


class ParseThread(Thread):
    def __init__(self,crawl_name,page_queue,data_queue,lock,fp):
        super().__init__()
        self.crawl_name = crawl_name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.lock = lock
        self.fp = fp

        while 1:
            content = self.data_queue.get()
            self.parse_data_queue(content)

    def parse_data_queue(self,content):
        soup = BeautifulSoup(content,'lxml')
        # 解析网页
        data = soup.

        # 先加锁
        self.lock.acquire()
        # 写入文件
        self.fp.write()

def creat_queue():
    page_queue = Queue()
    for page in range(1,10):
        page_queue.put(page)
    data_queue = Queue()
    return page_queue,data_queue






def main():
    '''
        主线程功能
        创建队列,页码队列,数据队列
        创建采集线程
        创建解析线程
        启动线程
        主线程等待

    :return:
    '''
    fp = open('fanjian.txt','w',encoding='utf8')

    lock = Lock()
    page_queue, data_queue = creat_queue()
    # 创建线程列表,保存所有线程
    t_crawl_list = []
    t_parse_list = []
    # 创建所有的采集线程
    crawl_name_list = ['采集线程1','采集线程2','采集线程3']
    for crawl_name in crawl_name_list:
        # 实例化线程对象
        t_crawl = CrawlThread(crawl_name,page_queue,data_queue)
        t_crawl_list.append(t_crawl)
        t_crawl.start()

    # 创建解析线程,并且启动
    parse_name_list = ['解析线程1', '解析线程2', '解析线程3']
    for parse_name in parse_name_list:
        # 实例化线程对象
        t_parse = ParseThread(parse_name, page_queue, data_queue,lock,fp)
        t_parse_list.append(t_parse)
        t_parse.start()
    # 主线程等待子线程
    for t_crawl in t_crawl_list:
        t_crawl.join()
    for t_parse in t_parse_list:
        t_parse.join()
    fp.close()

if __name__ == '__main__':
    main()