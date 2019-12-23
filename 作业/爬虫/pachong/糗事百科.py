# import urllib.request
# import urllib.parse
#
# '''
#     拼接url 发送请求 得到响应内容 分析响应内容 保存数据
# '''
# def ger_request(url):
#     headers = {
#         "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
#     return urllib.request.Request(url = url, headers = headers)
#
#
# def get_content(request):
#     return urllib.request.urlopen(request)
#
#
#
# def main():
#     start_page =int(input('input start page:\n'))
#     end_page = int(input('input end page'))
#     url = 'https://www.qiushibaike.com/pic/page/'
#     # 拼接url
#     for page in range(start_page, end_page + 1):
#         new_url = url + str(page) + '/'
#         request = ger_request(new_url)
#         response = get_content(request)
#
# if __name__ == '__main__':
#     main()
import requests,urllib.request
from lxml import etree

def get_request(url):
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'}
    r=requests.get(url,headers=header)
    return r.text

def get_img_html(text):
    html = etree.HTML(text)
    name = html.xpath('//div[@class = "content"]/span/text()')
    img_src = html.xpath('//div[@class = "thumb"]/a/img/@src')
    return [name,img_src]
def main():
    url = 'https://www.qiushibaike.com/pic/page/2/'
    text = get_request(url)
    url_list = get_img_html(text)
    url_li = ['https:' + i for i in url_list[1]]
    for a, b in zip(url_list[0],url_li):
        print(a + '\n' + b + '\n')
    # urllib.request.urlretrieve(str(url_list[0]), '1.jpg')
if __name__ == '__main__':
    main()
