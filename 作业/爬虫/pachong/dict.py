# -*- encoding: utf-8 -*-
"""
@Time    : 2019/8/15 18:15
@File    : dict.py
@Author  : huanyue
@Email   : ******@gmail.com
@IDE     : PyCharm
"""
import os,time

print(os.getcwd()+'/51job_shanghai_python.txt')
page_count =3
for page in range(page_count):
    print(page + 1,page_count)
    if page + 1 < page_count:
        time.sleep(3)