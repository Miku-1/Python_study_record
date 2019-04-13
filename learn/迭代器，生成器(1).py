'''生成器'''
# # a=[]
# # for i in range(10):
# #     a.append(i*2)
# # print(a)
# # a=(i*2 for i in range(10))
# # for i in a:
# #     print(i)
# # print(a.__next__())
# # print(a.__next__())
# # print(a.__next__())
# #0,1,1,2,3,5,8,13,21....
#
# def fib(Max):
#     n,a,b=0,0,1
#     while n<Max:
#         # print(b)
#         yield b
#         a,b=b,a+b
#         n+=1
#     return "done"
#
# f=fib(5)
# while True:
#     try:
#         x=next(f)
#         print("fff:",x)
#     except StopIteration as e:
#         print("生成器此时没有数据了。",e.value)
#         break
#
#
#
#
#
'''迭代器'''

#集合数据类型，列表，元组，字典，字符串。
#直接可用于for循环的对象统称为可迭代对象。（Iterable）

'''可以直接用于for循环的对象是可迭代对象'''
# from collections import Iterable
#
# print(isinstance([],Iterable))    #可判断该对象是不是可迭代对象
# print(isinstance("abc",Iterable))
# print(isinstance({},Iterable))
# print(isinstance((x for x in range(10)),Iterable))
# print(isinstance(100,Iterable))

'''可以直接用于for循环，并且
可以使用next()返回写一个值的对象称为迭代器'''

#Iterator  #迭代器
# from collections import Iterator
#
# print(isinstance([],Iterator))    #可判断该对象是不是迭代器
# print(isinstance("abc",Iterator))
# print(isinstance({},Iterator))
# print(isinstance((x for x in range(10)),Iterator))
# print(isinstance(100,Iterator))

#所以说，可迭代对象，不一定是迭代器

from collections import Iterator

# print(isinstance(iter([]),Iterator))    #可判断该对象是不是迭代器
# print(isinstance(iter("abc"),Iterator))
# print(isinstance(iter({}),Iterator))
# print(isinstance((x for x in range(10)),Iterator))
# print(isinstance(100,Iterator))

# List=[2,3,4,5,1]
# it=iter(List)
# print(next(it))

# for i in range(10):
#     print(i)

it=iter(range(10))
while True:
    print(next(it))