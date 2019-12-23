import urllib.request
# 创建handler
handler = urllib.request.ProxyHandler(proxies={'https':'182.92.169.109:3128'})
opener = urllib.request.build_opener(handler)
url = 'https://www.baidu.com'
# 这个opener有个open方法,类似urlopen
response = opener.open(url)
print(response.getcode())

# n, a = map(int,input('请输入两个值,用空格隔开').split(' '))
# arr =[int(i) for i in input('请输入三个值,用空格隔开').split(' ')]

# def GCU(m, n):
#     if not m:
#         return n
#     elif not n:
#         return m
#     elif m is n:
#         return m
#
#     while m != n:
#         if m > n:
#             m -= n
#         else:
#             n -= m
#     return m
# for i in range(n):
#     if arr[i] < a:
#         a += arr[i]
#     else:
#         a += GCU(a, arr[i])

