# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:59:48 2017

@author: Administrator

问题：如何派生内置不可变类型并修改其实例化行为
定义类intTuple继承内置tuple，并实现__new__,修改实例化行为。
注意：new方法是先于init方法执行的
"""

class IntTuple(tuple):
    
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0) # 定义生成器
        return super(IntTuple, cls).__new__(cls, g)
    
    def __init__(self, iterable):
        print self
        super(IntTuple, self).__init__(iterable)
        
if __name__=="__main__":
    t = IntTuple([1, -1, 'abc', 6, ['x','y'], 3])
    print t
