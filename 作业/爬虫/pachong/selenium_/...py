# import requests,json
# from bs4 import BeautifulSoup
# from time import sleep
#
# fp =open('fanjian.txt','w',encoding='utf8')
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
# }
# url = 'http://www.fanjian.net/jianwen-2'
# r = requests.get(url =url,headers=headers)
# soup = BeautifulSoup(r.text,'lxml')
# text_list = soup.select('.cont-list-title')[0]
# string = ''
# # for text in text_list:
# #     print(text.string)
# #     string += text.string + '\n'
# # fp.write(string)
# # print(string)
# print(text_list)
# fp.close()



# 有效括号
# s = "{}"
# def isVaild(s):
#     if len(s) % 2 == 1:
#         return False
#     stack = []
#     left = ['(', '[', '{']
#     right = [')', ']', '}']
#     dic = {
#         ')':'(',
#         ']':'[',
#         '}':'{'
#     }
#     for i in s:
#         if i in left:
#             stack.append(i)
#         elif i in right and len(stack) > 0:
#             temp = stack.pop()
#             if dic[i] != temp:
#                 return False
#         else:
#             return False
#     return len(stack) == 0
# print(isVaild(s))

# 最长公共前缀
# strs = ["flower","flow","floght","lokt"]
strs = ['12']
def longst(strs):
    if not strs:
        return ''
    str_min = min(strs)
    str_max = max(strs)
    for i in range(len(str_min)):
        if str_min[:i] != str_max[:i]:
            return str_min[:i]
print(longst(strs))







