# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 23:13:43 2017

@author: Administrator

问题：如何在环状数据结构中管理内存
使用标准库weakref，它可以创建一种能访问对象但不增加引用计数的对象
调用时需要像调用方法那样调用
"""

import weakref

class Data(object):
    def __init__(self, value, owner):
        self. owner = weakref.ref(owner)
        self.value = value
    
    def __str__(self):
        return "%s's data, value is %s" % (self.owner(), self.value)
    
    def __del__(self):
        print 'in Data.__del__'

class Node(object):
    def __init__(self, value):
        self.data = Data(value, self)
    
    def __del__(self):
        print 'in Node.__del__'

if __name__=='__main__':
    node = Node(100)
    del node # 同时删除Node和Data

