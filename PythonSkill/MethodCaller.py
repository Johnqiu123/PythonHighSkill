# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 13:15:13 2017

@author: Administrator

问题：如何通过实例方法名字的字符串调用方法
【方法一】使用内置函数getattr，通过名字在实例上获取方法对象，然后调用
【方法二】使用标准库operator下的methodcaller函数调用
"""
from operator import methodcaller
class Circle(object):
    """圆形"""
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return self.r ** 2 * 3.14

class Rectangle(object):
    """矩形"""
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def get_area(self):
        return self.w * self.h

class Ttriangle(object):
    """三角形"""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def getArea(self):
        a, b, c = self.a, self.b, self.c
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area

def getArea(shape):
    """统计求面积的方法"""
    for name in ('area','getArea','get_area'):
        f = getattr(shape, name, None) # 返回属性不为空的值
        if f:
            # 方法一
#            return f()
            # 方法二
            return methodcaller(name)(shape)
       

if __name__=='__main__':
    shape1 = Circle(2)
    shape2 = Ttriangle(3,4,5)
    shape3 = Rectangle(6,4)
    
    shapes = [shape1, shape2, shape3]
    print map(getArea, shapes)