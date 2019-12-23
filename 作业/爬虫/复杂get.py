import urllib.request
import urllib.parse
import os,time


# 输入贴吧名字 起始页码终止页码
bname = input('请输入贴吧名字\n')
startpage = int(input('请输入起始页码\n'))
endpage = int(input('请输入终止页码\n'))
if not os.path.exists(bname):
    os.mkdir(bname)
url = 'http://tieba.baidu.com/f?'
# 通过循环拼接每一页的url,得到每一页的内容
for page in range(startpage,endpage+1):
    pn =(page - 1)* 50
    data = {
        'kw':bname,
        'ie':'utf8',
        'pn':pn
    }
    query_string = urllib.parse.urlencode(data)
    # 拼接得到url
    print(type(query_string))
    newurl = url +query_string
    # print(newurl)
    # 构建对象
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12'}

    # 发送请求
    request = urllib.request.Request(url = newurl,headers = headers)
    # 得到响应
    response = urllib.request.urlopen(request)
    # 生成文件名
    filename = '{}第{}页.html'.format({'贴吧名字':bname},{page})
    # 拼接文件路径
    filepath = os.path.join\
        (bname,filename)
    # 将内容写到filepath中
    with open(filepath,'wb')as f:
        f.write(response.read())
    time.sleep(2)