# # -*- encoding: utf-8 -*-
# """
#     @Time   : 2019/8/16 18:21
#     @File   : jingdong_pinglun.py
#     @Author : huanyue
#     @Email  : huanyue521@gmail.com
#     @IDE    : PyCharm
#     @Task   爬取京东某一产品下的评论
# """
# import requests,json
# import urllib.parse
# query = {"operationName":"videoFeedsQuery","variables":{"count":20},"query":"fragment VideoMainInfo on VideoFeed {\n  photoId\n  caption\n  thumbnailUrl\n  poster\n  viewCount\n  likeCount\n  commentCount\n  timestamp\n  workType\n  type\n  useVideoPlayer\n  imgUrls\n  imgSizes\n  magicFace\n  musicName\n  location\n  liked\n  onlyFollowerCanComment\n  width\n  height\n  expTag\n  __typename\n}\n\nquery videoFeedsQuery($pcursor: String, $count: Int) {\n  videoFeeds(pcursor: $pcursor, count: $count) {\n    list {\n      user {\n        id\n        eid\n        profile\n        name\n        __typename\n      }\n      ...VideoMainInfo\n      __typename\n    }\n    pcursor\n    __typename\n  }\n}\n"}
# url = 'https://live.kuaishou.com/graphql'
# headers = {
#     'accept':'*/*',
#     'content-type': 'application/json',
#     'Referer': 'https://live.kuaishou.com/v/hot/',
#     'Sec-Fetch-Mode': 'cors',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
# }
# url = url + urllib.parse.urlencode(query)
# # 获取网页信息
# req=requests.get(url ,timeout=30,headers=headers)
#
# jd=json.loads(req.text)
# print(jd)
#
import urllib.parse
import urllib.request
import json,jsonpath

def gethtml(url):
    headers = {
        'accept': '*/*',
        'content-type': 'application/json',
        'Referer': 'https://live.kuaishou.com/v/hot/',
        'Sec-Fetch-Mode': 'cors',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
    request = urllib.request.Request(url=url,headers=headers)
    content = urllib.request.urlopen(request).read().decode('utf8')
    return content
query_string = {"operationName":"videoFeedsQuery",
                "variables":{"count":20},
                "query":"fragment VideoMainInfo on VideoFeed {\n  photoId\n  caption\n  thumbnailUrl\n  poster\n  viewCount\n  likeCount\n  commentCount\n  timestamp\n  workType\n  type\n  useVideoPlayer\n  imgUrls\n  imgSizes\n  magicFace\n  musicName\n  location\n  liked\n  onlyFollowerCanComment\n  width\n  height\n  expTag\n  __typename\n}\n\nquery videoFeedsQuery($pcursor: String, $count: Int) {\n  videoFeeds(pcursor: $pcursor, count: $count) {\n    list {\n      user {\n        id\n        eid\n        profile\n        name\n        __typename\n      }\n      ...VideoMainInfo\n      __typename\n    }\n    pcursor\n    __typename\n  }\n}\n"}

url ='https://live.kuaishou.com/graphql'
url = url + urllib.parse.urlencode(query_string)
content = gethtml(url)
print(content)
