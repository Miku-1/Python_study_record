# -*- encoding: utf-8 -*-
"""
    @Time   : 2019/8/16 15:13
    @File   : json_1.py
    @Author : huanyue
    @Email  : huanyue521@gmail.com
    @IDE    : PyCharm
    @Task
"""

# 定义结点
class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleListTable():
    # 初始化头节点为空
    def  __init__(self):
        self.head = None

    # 链表头部添加结点
    def add(self,value):
        node = Node(value)
        node.next = None
        self.head = node

    # 链表尾部添加结点
    def append(self,value):
        node = Node(value)
        cur = self.head
        # 判断是否空链表
        if not cur:
            self.head = node
        else:
            while cur.next:
                cur = cur.next
            cur.next = node

    # 链表的插入


    # 链表的修改


    # 链表的删除


    # 链表的查找