# -*- encoding: utf-8 -*-
"""
    @Time   : 2019年8月20日 上午10:28
    @File   : 1-login.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
import requests
from bs4 import BeautifulSoup
# 创建会话

s = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
# 向登录界面发送请求,获取图片链接
url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
r = s.get(url=url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
# 找到图片src
image_src = 'https://so.gushiwen.org/ '+ soup.find('img', id='imgCode')['src']
# 下载保存
img_ret = s.get(url=image_src,headers=headers)
with open('code.png','wb')as f:
    f.write(img_ret.content)
# 获取表单隐藏值
viewstate = soup.find('input', id='')['value']
viewg = soup.find('input', id='')['value']
code = input('请输入验证码:\n')

# 发送post请求
post_url = ''


formdata = {

}

r = s.post(url =post_url,data=formdata)






