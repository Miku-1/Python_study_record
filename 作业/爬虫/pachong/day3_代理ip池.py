import time
import random#简易ip池
arr = [
    '39.137.69.9:8080',
    '119.57.108.109:53281',
    '124.207.82.166:8008',
    '221.223.46.37:8060',
    '114.115.213.9:8888',
    '116.196.90.181:3128',
    '221.216.141.209:9000',
    '123.206.44.121:80',
    '47.94.104.204:8118',
    '182.92.169.109:3128'

]
import urllib.request

# # 随机从文件中读取一个代理
# file = open('daili.txt','r')
# content = file.read()
# # 将内容分割
# lt =content.split('\n')
# print(lt)
#
# while 1:
#     # 随机抽取1个代理，拼接格式
#     daili = random.choice(lt)
#     handler = urllib.request.ProxyHandler(proxies={'https':daili})
#     opener = urllib.request.build_opener(handler)
#     url = 'https://www.baidu.com'
#     try:
#         response = opener.open(url)
#         print(f'代理使用成功{daili}')
#         with open('dailiurl','wb')as f:
#             f.write(response.read())
#     except Exception as e :
#         print('代理使用失败')
#         lt.remove(daili)
#         print(e)
#         time.sleep(2)
import base64
url = ''
user = 'fsfdf' #通行证账号
pwd  = 'sdsf' #密码
sstr = user + ':' + pwd
# 将指定的字符串进行base64编码
encodestr = 'Basic '+base64.b64encode(sstr.encode('utf-8')).decode('utf-8')
print(encodestr)

headers = {
    'Proxy-Authorization':encodestr
}

# 构建请求对象
request = urllib.request.Request(url=url,headers = headers)
# 构建handle，opener
proxy = {'http-pro.abuyun.com':'9020'}
handler = urllib.request.ProxyHandler(proxies=proxy)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
print(response.read().decode('utf-8'))