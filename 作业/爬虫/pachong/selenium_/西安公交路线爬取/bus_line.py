# -*- encoding: utf-8 -*-
"""
    @Time   : 2019/8/18 16:09
    @File   : main.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
import requests,json
from time import sleep
from bs4 import BeautifulSoup
from xpinyin import Pinyin

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
# 处理一级界面
def parse_first_page(url):

    # 处理一级界面
    r = requests.get(url=url,headers=headers)
    # 生成对象
    soup = BeautifulSoup(r.text,'lxml')
    # 得到数字开头的a链接
    number_href_list = soup.select('.bus_kt_r1 > a')
    # 得到字母开头的a链接
    char_href_list = soup.select('.bus_kt_r2 > a')
    all_a_list = number_href_list + char_href_list
    all_href_list = []
    # 提取链接
    for oa in all_a_list:
        # 添加协议主机
        href_url = url.rstrip('/')+oa['href']
        all_href_list.append(href_url)
    return all_href_list

def parse_second_page(all_href_list, url):
    # 遍历,并依次发送请求
    all_list = []
    for href in all_href_list:
        r = requests.get(url = href,headers = headers)
        # 解析
        soup = BeautifulSoup(r.text, 'lxml')
        # 提取详细公交的链接
        odiv = soup.find('div',id='con_site_1')
        # 查找odiv下的所有a链接
        oa_list = odiv.find_all('a')
        # 提取所有a对象href
        oa_href_list = []
        for oa in oa_list:
            href = url.rstrip('/') + oa['href']
            oa_href_list.append(href)
        sleep(1)
        all_list += oa_href_list
    return all_list

def parse_third_page(oa_href_list,fp):
    for href in oa_href_list:
        r = requests.get(url=href,headers=headers)
        soup = BeautifulSoup(r.text,'lxml')
        row_name = soup.select('.bus_i_t1 > h1')[0].text.strip('&nbsp')
        run_time = soup.select('.bus_i_content > .bus_i_t4')[0].string.strip('运行时间：')
        price_info = soup.select('.bus_i_content > .bus_i_t4')[1].string.lstrip('票价信息：')

        bus_company = soup.select('.bus_i_content > .bus_i_t4 > a')[0].string
        # 上行总站数,
        up_total = soup.select('.bus_line_no')[0].string.strip('共站').strip()

        up_div = soup.select('.bus_line_site')[0]
        up_total_list = up_div.select('div > a')
        up_name_list = []
        # 遍历，获取所有名字
        for oa in up_total_list:
            up_name_list.append(oa.string)
        try:
            # 下行总站数
            down_total = soup.select('.bus_line_top > span ')[1].string.strip('共站').strip()
            # 获取下行总站牌
            down_div = soup.select('.bus_line_site')[1]
            down_total_list = down_div.select('div > a')
            down_name_list = []
            # 遍历，获取所有名字
            for oa in down_total_list:
                down_name_list.append(oa.string)
        except Exception as e:
            down_total = "无下行线路"
            down_name_list = []

        #保存到字典中
        item = {
            '线路名称': row_name,
            '运行时间': run_time,
            '票价信息': price_info,
            '公司信息': bus_company,
            '上行总站数':up_total,
            '上行总站牌':up_name_list,
            '下行总站数':down_total,
            '下行总站牌':down_name_list

        }
        string = json.dumps(item,ensure_ascii=False)
        print(f'正在保存---{row_name}---信息')
        fp.write(string + '\n')
        print('Success')
        sleep(2)

def main():
    city = input('请输入你要查找的城市名字\n')
    city_pinyin = Pinyin().get_pinyin(city).replace('-','')
    fp = open('{}公交.txt'.format(city),'w',encoding='utf8')
    url = 'https://{}.8684.cn'.format(city_pinyin)
    # 解析一级节点 parse_first_page
    first_page = parse_first_page(url)
    # 解析二级节点
    second_page = parse_second_page(first_page, url)
    # 解析三级节点
    parse_third_page(second_page,fp)
    fp.close()

if __name__ == '__main__':
    main()