# -*- encoding: utf-8 -*-
"""
    @Time   : 2019年8月19日 下午11:43
    @File   : 多线程.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
from queue import Queue
import threading
import requests
from bs4 import BeautifulSoup
import time


# 采集线程
class CrawlThread(threading.Thread):
    def __init__(self, crawl_name, page_queue, data_queue):
        super().__init__()
        self.crawl_name = crawl_name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.url = 'http://www.fanjian.net/jianwen-{}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        }

    def run(self):
        '''
        1.从页码队列中去一个page
        2.和url拼接为一个完整的url
        3.发送请求，得到响应数据
        4.将响应数据存储到数据队列中
        '''
        while True:
            try:
                page = self.page_queue.get(False)
                url = self.url.format(page)
                r = requests.get(url=url, headers=self.headers)
                # 将内容写入数据队列(data_queue)
                self.data_queue.put(r.text)
            except:
                break
        print('%s线程结束------' % self.crawl_name)


class ParseThread(threading.Thread):
    def __init__(self, parse_name, data_queue, fp, lock):
        super().__init__()
        self.parse_name = parse_name
        self.data_queue = data_queue
        self.fp = fp
        self.lock = lock

    def run(self):
        '''
        1.从数据队列中去取一页数据
        2.解析数据并保存
        '''
        while 1:
            try:
                content = self.data_queue.get(False)
                # 解析放到函数里面去做
                self.parse_data_queue(content)
                time.sleep(5)
            except:
                break
        print('%s线程结束------' % self.parse_name)

    def parse_data_queue(self, content):
        soup = BeautifulSoup(content, 'lxml')
        # 解析网页
        text_list = soup.select('.cont-list-title')
        # 先加锁
        self.lock.acquire()
        # 写入文件
        string = ''
        for text in text_list:
            string += text.string + '\n'
        # print(string)
        print('正在写入')
        self.fp.write(string)
        print('-------')
        # 解锁
        self.lock.release()


def creat_queue():
    page_queue = Queue()
    for page in range(1, 10):
        page_queue.put(page)
    data_queue = Queue()
    return page_queue, data_queue


def main():
    '''
    主线程的功能都有哪些？
    创建队列，页码队列，数据队列
    1.创建采集线程
    2.创建解析线程
    3.启动线程
    4.主线程等待

    ?打开文件，线程锁
    '''
    fp = open('犯贱.txt', 'a', encoding='utf8')

    lock = threading.Lock()
    page_queue, data_queue = creat_queue()
    # 创建列表保存所有的线程
    t_crawl_list = []
    t_parse_list = []

    # 创建所有的采集线程，并且启动之
    crawl_name_list = ['采集线程1', '采集线程2', '采集线程3']
    for crawl_name in crawl_name_list:
        # 实例化线程对象（创建线程）
        print(crawl_name)
        t_crwal = CrawlThread(crawl_name, page_queue, data_queue)
        t_crawl_list.append(t_crwal)
        t_crwal.start()

    # 创建解析线程，并且启动之
    parse_name_list = ['解析线程1', '解析线程2', '解析线程3']
    for parse_name in parse_name_list:
        # 实例化线程对象（创建线程）
        t_parse = ParseThread(parse_name, data_queue, fp, lock)
        # print(parse_name)
        t_parse.start()
        t_parse_list.append(t_parse)



    # 主线程等待子线程
    for t_crwal in t_crawl_list:
        print(t_crwal.crawl_name)
        t_crwal.join()

    for t_parse in t_parse_list:
        t_parse.join()
        # print(t_parse.parse_name)

    fp.close()
    print('主线程-子线程全部结束')


if __name__ == '__main__':
    main()