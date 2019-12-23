import urllib.request
url = 'http://www.renren.com/971911578/profile'
headers ={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
'Cookie': 'anonymid=jzapajc6vpdl2b; depovince=SXI; _r01_=1; JSESSIONID=abcNU1F35MlDE_CfjmoYw; ick_login=7ead674b-1cf0-47b3-b964-d0c3b38b72c7; ick=851acdcb-b5f2-4726-9fcd-c266935fba98; t=a4c399b7a9e51723edf1b34bd5e2bee68; societyguester=a4c399b7a9e51723edf1b34bd5e2bee68; id=971911578; xnsid=71ce5594; XNESSESSIONID=d0ce9cf51cb2; ver=7.0; loginfrom=null; wp_fold=0; jebecookies=52955053-57b8-4f80-bb26-f0d94860142b|||||'
}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
# print(response.read().decode('utf8'))
# with open('renren.html','w')as f:
#     f.write(response.read().decode('utf8'))


