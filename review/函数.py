import datetime
# 装饰器
# 在不改变被装饰函数的源代码和调用方式的前提下，为被装饰的函数增加新的功能
# 装饰器的实质,
# 装饰器对被装饰函数功能添加的实质是把被装饰函数的内存地址替换为另一个函数的内存地址，以后只要执行装饰函数的函数()名实际上执行替换过函数的地址。
# 而装饰器函数内部一方面执行了原来被装饰函数的函数体，同时也新添加了部分代码，从而实现了对被装饰函数功能的添加。
# def now_time(func):
#     print('当前时间')
#     def wrapper(a, b):
#         print(datetime.datetime.now().strftime('%F %T'))
#         func(a,b)
#     return wrapper
# @now_time
# def add(a, b):
#     print(a + b)
# add(5,6)

