'''d={key1:value1,key2:value2}'''
'''key(键)，必须唯一，value(值)，可以重复'''
'''字典是无序的'''
# d={3:"three",2:"two",4:"four",1:"one"}
# print(d)
#1、查字典(一定要确定有该键)
# d = {1 : "one",2 : "two",3 : "three",4 : "one",5 : "two"}
# print(d[2])

#2、增加
# d = {1 : "one",2 : "two",3 : "three",4 : "one"}
# d[5]="a"
# print(d)

#3、删除
# d = {1 : "one",2 : "two",3 : "three",4 : "one"}
# del d
# print(d)

#标准删除
# d = {1 : "one",2 : "two",3 : "three",4 : "one"}
# a=d.pop(2)
# print(d)
# print(a)

# d = {1 : "one",2 : "two",3 : "three",4 : "one"}
# d.popitem()   #随机删除
# print(d)

#4、查找2
d = {1 : "one",2 : "two",3 : "three",4 : "one"}
# print(d.get(2))
print(4 in d)   #判断d中是否存在该键值

#5、打印所有的值
# d = {1 : "one",2 : "two",3 : "three",4 : "one"}
# print(d.values())

#6、打印所有的键
# d = {1 : "one",2 : "two",3 : "three",4 : "one"}
# print(d.keys())

#7、字典拼接
# d1={3:"three",2:"two",4:"four",1:"one"}
# d2={5:"three",6:"two",7:"four",8:"one"}
# d1.update(d2)
# print(d1)

#8、打印所有项
# d={3:"three",2:"two",4:"four",1:"one"}
# print(d.items())

#9、字典初始化
# c=dict.fromkeys([2,3,4],"+++")
# print(c)

'''fromkeys现象说明'''
# c=dict.fromkeys([6,7,8],[1,{"a":"A"},"feng"])
# print(c)
# c[7][1]["a"]="QQ"
# print(c)
# d1 = dict.fromkeys([1,"two",3])
# print(d1)
# d2 = dict.fromkeys([1,"two",3],"cool")
# print(d2)

# d={3:"three",2:"two",4:"four",1:"one"}

# for i in d:
#     print(d[i])

# for k,v in d.items():
    # print(k,v)

# d={'one':1,'two':2,'three':3}
# print(d)
# print(d.setdefault('one',1))
# print(d.setdefault('four',4))
# print(d)

# d={'one':1,'two':2,'three':3}
# print(d)
# d.pop('one')
# print(d)

# d={'one':1,'two':2,'three':3,"four":4}
# print(d)
# d.popitem()
# print(d)
d={'one':1,'two':2,'three':3,"four":4}
# it=d.__iter__()
# for x in it:
#     print(x)