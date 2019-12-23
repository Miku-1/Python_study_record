import urllib.request
import urllib.parse
import random

ajax_url = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&'
page = int(input('请输入要获取的页数'))
query_string = {
    'start':'0',
    'limit':20*page,
}
# 拼接url
query_string = urllib.parse.urlencode(query_string)
ajax_url += query_string
# 构建请求对象
headers= [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'},
				{'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12'},
				{'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0'}]
headers =random.sample(headers,1)[0]
# # 请求对象
request = urllib.request.Request(url = ajax_url,headers = headers)
response = urllib.request.urlopen(request)
with open('douban.html','wb')as f :
    f.write(response.read())