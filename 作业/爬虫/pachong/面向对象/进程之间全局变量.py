# -*- encoding: utf-8 -*-
"""
    @Time   : 2019年8月19日 上午10:50
    @File   : 进程之间全局变量.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""


from multiprocessing import Process

x = 1

def demo():
    global x
    x += 1
    print(f'x={x}')


if __name__ == '__main__':
    p1 = Process(target=demo)
    p1.start()
    p1.join()
    print(f'x={x}')

