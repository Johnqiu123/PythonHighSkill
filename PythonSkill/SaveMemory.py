# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:10:42 2017

@author: Administrator

问题：如何为创建大量实例节省内存
定义类的__slots__属性，它是用来声明实例属性名字的列表

思路：找出内存开销的主要原因，然后解决该原因
关键问题：'__dict__'
解决：使用__slots__固定属性
"""

class Player(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

class Player2(object):
    __slots__ = ['uid','name','stat','level'] # 固定绑定
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

if __name__=='__main__':

    import sys
    # 找出开销的原因
    p1 = Player('0001', 'Jim')
    p2 = Player2('0001', 'Jim')
    
    # '__dict__'
    print set(dir(p1)) - set(dir(p2)) # 相差的属性：set(['__dict__', '__weakref__'])
    print p1.__dict__ # 动态绑定字典
    
    # 自动绑定字典
    p1.x = 1
    print p1.__dict__
    print sys.getsizeof(p1.__dict__) # 占了272
    
#    p2.x = 1 # 固定绑定
#    print p2.__dict__
       