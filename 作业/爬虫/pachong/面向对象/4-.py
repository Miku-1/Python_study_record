# -*- encoding: utf-8 -*-
"""
    @Time   : 2019年8月19日 下午2:23
    @File   : 4-.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""
import threading
from time import sleep
# def sing():
#     for x in range(1,6):
#         print(f'sing线程名{threading.current_thread().name}')
#         print('我喜欢唱山歌')
#         sleep(1)
# def dance(name):
#     for i in range(1,6):
#         print(f'dance线程名{threading.current_thread().name}')
#         print(f'{name}你喜欢蹦迪')
#         sleep(1)
#
# def main():
#     name = '贾玲'
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance,args=(name,))
#     t1.start()
#     t2.start()
# if __name__ == '__main__':
#     main()


class singThreading(threading):
    def run(self):
        for x in range(1,6):
            print()
            print('我喜欢唱歌')
            sleep(1)

class danceThreading(threading):
    def run(self):
        for i in range(1, 6):
            print(f'dance线程名{threading.current_thread().name}')
            print('{}你喜欢蹦迪')
            sleep(1)

def main():
    t1 = singThreading()
    t2 = danceThreading()
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
















