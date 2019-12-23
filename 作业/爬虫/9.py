import urllib.request

url = 'https://www.baidu.com/'

# 创建一个handler对象
handler = urllib.request.HTTPSHandler()

# 创建一个opener
opener = urllib.request.build_opener(handler)
# 这个opener有个open方法,类似urlopen
response = opener.open(url)
print(response.read().decode('utf-8'))
