# def func(x,y,f):
#     return f(x)+f(y)
# print(func(-1,9,abs))

# 1、all函数，判断对象，如果都为True，就返回True
# print(all(["jfdks",2,3,1]))
# print(all([0,3,1]))

#2、可迭代对象中或者集合中，任意的一个数据为真，
# 就返回zhen
# print(any([37,0,3]))
# print(any([0,0]))

#3、ascii()
# a = ascii(12)
# print(a)
# print(type(a))

#4、将十进制转换成二进制
# print(bin(8978))
# print(type(bin(8978)))

# print(oct(8978))
# print(type(oct(8978)))

# print(hex(89))
# print(type(hex(89)))

# a = dict()
# print(a)
# b = dict((("1",1),("2",2)))
# print(b)
# c = dict((["a","b"],[1,2]))
# print(c)

# a = set()
# print(a)
# b = set(range(10))
# print(b)
# c = set("ab122")
# print(c)

# color = ["red","green","yellow","bule"]
# print(list(enumerate(color)))
# print(list(enumerate(color,start=2)))



#5、布尔方法
# print(bool([1]))
# print(bool([8]))

#6、字节数组
# a = bytes("abcdef",encoding="utf-8")
# print(a)
# b = bytes("栗子",encoding="utf-8")
# print(b)

# a = memoryview(b'abcde')
# print(a)
# print(a[-1])

# b = bytearray("abcdef",encoding="utf-8")
# print(b[0])
# print(b)

#7、判断是否可调用
# def func(x,y,f):
#     return f(x)+f(y)
# print(callable(func))

#8、利用数字得到Ascii码对应字符
# print(chr(97))
# print(chr(165))

#9、利用字符得到Ascii码对应的数字
# print(ord("b"))
# print(ord("A"))

#10、查看对象的方法
# print(dir([]))

# a = "lizi"
# print(id(a))

#11、地板除
# print(divmod(5,2))

#12、对应下标
# for i,v in enumerate([2,3,4,5,6,7,8,9]):
#     print(i,v)

#13、将字符串变为可执行语句
# print(eval("3*7"))   #只能执行简单语句
# print(eval("for i in range(5):print(i)"))   #只能执行简单语句
#
# exec('''for i in range(5):print(i)''')

#14、过滤数据
# y=lambda x:abs(x)
# print((lambda x: x if x<5 else 5)(7))
# print((lambda a, b :a*b if a < b else a+b)(5,6))
#filter,将满足情况的项输出，
#map，将判断结果输出

# ve=filter(lambda n:n>5,range(10))
# for i in ve:
#     print(i)
# re=map(lambda n:n>5,range(3))
# for i in re:
#     print(i)

#15、
# import functools
# res=functools.reduce(lambda x,y:x*y,range(1,9))
# print(res)
# l=[]
# for i in range(1,10):
#     l.append(str(i))
# #
# res="*".join(l)
# print(res)
# print(eval(res))

# def res(x):
#     Num=1
#     for i in range(1,x+1):
#         Num=Num*i
#     return Num
    # if x == 0 or x == 1:
    #     return 1
    # else:
    #     return x*res(x-1)

# print(res(9))


#16、冻结集合
# a=set([2,3,4])
# print(a)

# a=frozenset([2,3,4])
# print(a)
# # a[2]="aaa" #TypeError: 'frozenset' object does not support item assignment

#17、查找哈希表
# print(hash("a"))

#18、将十进制转换成十六进制
# print(hex(123))

#19、判断对象是否是已知类型
# a=1
# print(isinstance(a,int))
# print(type(1))

# print(type(1))

# type和isinstance的区别
# type不认为子类是一种父类类型，不考虑继承
# isinstance会认为子类是一种父类类型，考虑继承
# 如果需要判断两种类型的关系，建议使用isinstance

# class A(object):
#     pass
# class B(object):
#     pass
#
# print(isinstance(A(),A))
# print(type(A())==A)
# print(isinstance(B(),A))
# print(type(B())==A)


#20、打印局部变量
# a = 1
# def A():
#     varse=2347
#     print(globals())  # 返回本模块中所有的全局变量
#     # print(locals())   #打印局部变量
# print(A())


#21、最大值(最小值)
# print(min([2,3,4,5,6,7]))
# print(min([1,2],[2,3],[3,4]))
# a=[3,4,5,6,7,8,9,10,11]
# print(a.index(min(a)))        #index为元素下标，输出最大值所对应的元素下标
# print(min("aa","ab","ac"))    #按ASCII码中的数值大小
# print(min(-1,0,key=abs))      #abs为绝对值参数
# print(min(1,2,3,"4",key=int)) #转为int型进行比较


#22、幂运算
# print(2**3)
# print(pow(3,3))     #3**3
# print(pow(2,3,3))   #2**3%3

#23、设置小数保留位数
# print(round(1.734567))    #取四舍五入的值
# print(round(1.234565,3))  #四舍五入取三位


#24、排序
# a={1:2,3:4,9:2,8:6}
# print(sorted(a.items(),reverse=True))
# print(sorted(a.items(),key=lambda x:x[1]))

#25
# a=[1,2,3,4]
# b=[5,6,7,8]
# for i in zip(a,b):
#     print(i)

# a=[1,2,3]
# b=[5,6,7,8]
# for i in zip(a,b):
#     print(i)
#
# c=[[1,2,3],[4,5,6],[7,8,9]]
# for i in zip(*c):
#     print(i)

#求和
# a = sum((1,2,3,4))
# print(a)

#int类型
# a = int()
# print(a)
# b = int("3")
# print(b)
# c = int(3.2)
# print(c)

#float类型
# a = float()
# print(a)
# b = float("3")
# print(b)
# c = float(4)
# print(c)


# a = complex()
# print(a)
# b = complex(1,2)
# print(b)
# c = complex("1+2j")
# print(c)

# print(str(12))
# print(type(str(12)))
