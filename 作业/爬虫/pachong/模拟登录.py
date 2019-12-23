# import urllib.request
# import urllib.parse
# post_url = 'www.ajaxLogin/login?1=1&uniqueTimestamp=2019731440668'
# formdata = {
#
# }
import json
import requests
from lxml import etree
def url(n):
    url=f'http://maoyan.com/board/6?offset={n*10}'
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'}
    r=requests.get(url,headers=header)
    return r.text
