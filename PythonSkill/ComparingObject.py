# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 08:02:59 2017

@author: Administrator

问题：如何让类支持比较操作
比较符号运算符重载，需要实现一下方法：
__lt__,__le__,__gt__,__ge__,__eq__,__ne__
使用标准库下的functools下的类装饰器total_ordering可以简化此过程

只需实现__lt__和__eq__方法即可
"""
from functools import total_ordering
from abc import abstractmethod

@total_ordering
class Shape(object):
    """定义图形基类"""
    @abstractmethod
    def area(self):
        pass
    
    def __lt__(self, obj):
        print 'in __lt__'
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape')
        return self.area() < obj.area()
    
    def __eq__(self, obj):
        print 'in __eq__'
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape')
        return self.area() == obj.area()

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return self.r ** 2 * 3.14

if __name__ == '__main__':
    
    r1 = Rectangle(5, 3)
    r2 = Rectangle(4, 4)
    c1 = Circle(3)
    
    print  r1 <= r2
    print c1 <= r1
    print r1 > c1