#变量指向函数，函数可以接收参数。
# def Add(a,b,f):
#     return f(a)+f(b)
#
# print(Add(-2,-3,abs))   #abs(-2)+abs(-3)

#装饰器
'''
1、为原函数增加功能，但是不能修改原函数。
2、不能修改原函数调用方式。
'''
import time
def timmer(func):
    def Warp(*args,**kwargs):
        Start_time=time.time()
        func()
        Stop_time=time.time()
        print("the func runtime: %s" %
              (Stop_time-Start_time))
    return Warp

@timmer   #语法糖   test=timmer(test)
def test():
    time.sleep(3)
    print("in the test")

test()

# import time
# def bar():
#     time.sleep(3)
#     print("in the bar")
#
# def test(func):
#     Start_time=time.time()
#     func()
#     Stop_time=time.time()
#     print(Stop_time-Start_time)
#     return func
#
# bar=test(bar)   #return bar

# def foo():
#     print("in the foo")
#     def bar():
#         print("in the bar")
#
#     bar()
#
# foo()

# import time
#
# def timmer(func):
#     def foo(*args,**kwargs):
#         Start_time=time.time()
#         func(*args,**kwargs)
#         Stop_time=time.time()
#         print(Stop_time-Start_time)
#     return foo

# @timmer    #test=timmer(test)=foo
# def test():
#     time.sleep(3)
#     print("in the test")
    # print(x,y,z)

# test=timmer(test)
# test()   #foo()

# import time
# user,password="shanligong",1234
# def auth(func):
#     def foo(*args,**kwargs):
#         username=input("请输入账号：")
#         key=int(input("请输入密码："))
#         if user==username and password==key:
#             print("恭喜你，登录成功！！")
#         else:
#             print("您输入的密码或者账号错误！")
#     return foo
#
#
# def index():
#     print("in the index")
# @auth
# def home():
#     print("in the home")
# @auth
# def bbs():
#     print("in the bbs")
#
# index()
# home()
# bbs()



