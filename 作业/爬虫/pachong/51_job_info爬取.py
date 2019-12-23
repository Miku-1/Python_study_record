# -*- encoding: utf-8 -*-
"""
    @Time    : 2019/8/15 17:07
    @File    : 51_job_info爬取.py
    @Author  : huanyue
    @Email   : huanyue521@gmail.com
    @IDE     : PyCharm
    @Task    : 爬取51job指定页数的岗位信息
"""
from bs4 import BeautifulSoup
import urllib.request
import time,os

def gethtml(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    request = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(request)
    html = response.read().decode('gbk')
    return html

def parse_content(content):
    # 生成soup对象
    soup = BeautifulSoup(content,'lxml')
    # 查找所有的岗位信息
    # 岗位信息从列表从第十七个开始
    odiv_list = soup.find_all('div',class_ = 'el')[16:]
    print(len(odiv_list))
    fp = open('51job_shanghai_python开发.txt','a+',encoding='utf8')
    # 获取岗位信息,并保存
    for odiv in odiv_list:
        # 职位名
        job_name = odiv.find('a', target='_blank').text.strip()
        # 公司名
        company_name = odiv.find('span', class_='t2').text
        # 工作地点
        working_place = odiv.find('span', class_='t3').text
        #　薪资,如果没给出具体薪资,则记为'薪资待定
        salary = odiv.find('span', class_='t4').text
        if salary == '':
            salary = '薪资待定'
        #  发布时间
        release_time = odiv.find('span', class_='t5').text
        # 将每条信息存入字典
        job_info = {}
        job_info['职位名'] = job_name
        job_info['公司名'] = company_name
        job_info['工作地点'] = working_place
        job_info['薪资'] = salary
        job_info['发布时间'] = release_time
        # 将字典写入文件
        fp.write(str(job_info ) + '\n')
    fp.close()

def main():
    # url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,岗位信息,页码.html,'
    # url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,Python%20%E5%BC%80%E5%8F%91,2,'
    url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,Python%2B%25E7%2588%25AC%25E8%2599%25AB,2,'
    page_count = int(input('正在爬取上海python开发岗位信息,请输入要爬取的页数(ps:每页50条职位信息):\n'))

    for page in range(page_count):
        new_url = url + str(page + 1) + '.html'
        content = gethtml(new_url)
        print('正在保存第{}页内容'.format(page + 1))
        parse_content(content)
        print('Success'.format(page + 1))
        if page + 1 < page_count:
            time.sleep(3)
    print('任务完成')
    # os.startfile(os.getcwd()+'/51job_shanghai_python.txt')

if __name__ == '__main__':
    main()