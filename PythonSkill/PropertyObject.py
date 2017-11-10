# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 07:39:57 2017

@author: Administrator

问题：如何创建可管理的对象属性
使用property函数为类创建可管理属性，fget/fset/fdel对应相应属性访问
类似于Java的getter、setter方法
"""
from math import pi
class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    
    def getRadius(self):
        return self.radius
    
    def setRadius(self, value):
        if not isinstance(value, (int, long, float)):
            raise ValueError("wrong type.")
        self.radius = float(value)

    def getArea(self):
        return self.radius ** 2 * pi
    
    R = property(getRadius, setRadius)

if __name__=='__main__':
    c = Circle(3.2)
    print c.radius
    print c.R
    c.R = 'abc' # 增加属性的判断
    print c.R
#    c.radius = 'abc'
#    print c.radius
