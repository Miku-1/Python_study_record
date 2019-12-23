# import urllib.request
# import urllib.parse

# ajax_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
# cname = input('请输入要查询的城市\n')
# pageIndex = input('请输入要查询的页码\n')
# pageSize = input('请输入个数\n')
# formdata = {
#     'cname':cname,
#     'pid':'',
#     'pageIndex':pageIndex,
#     'pageSize': '10'
#糗事百科.py }
# # 处理表单数据
# formdata = urllib.parse.urlencode(formdata).encode('utf8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12'}
# request = urllib.request.Request(ajax_url,headers)
# response = urllib.request.urlopen(request,data=formdata)
# print(response.read().decode('utf8'))


import re
'''
	mathch pi
'''
import re
reg='\d+'
print(re.findall(reg,'1a2b3c4d5e6f7g'))