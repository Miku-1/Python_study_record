# -*- encoding: utf-8 -*-
"""
    @Time   : 2019年8月19日 上午10:15
    @File   : 面向对象.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
from multiprocessing import Process
from time import sleep
class SingProcess(Process):

    def run(self):
        for i in range(6):
            print('我在唱歌')
            sleep(1)

class DanceProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        for i in range(1,6):
            print(f'我在跳舞和{self.name}')
            sleep(1)
