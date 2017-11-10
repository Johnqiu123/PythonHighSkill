# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 09:18:14 2017

@author: Administrator

问题：如何为元组中的每个元素命名，提高程序可读性？
【方法一】定义类似与其他语言的枚举类型，也就是定义一系列数值常量
【方法二】使用标准库中collections.namedtuple替代内置tuple
"""
from collections import namedtuple

if __name__ == '__main__':
    
    # soluction 1
    # 给索引命名
    name, age, sex, email = range(4)
    
    student = ('Jim', 16, 'male', 'aa@gmail.com')
    
    # name
    print student[name]
    print student[age]
    
    ###################
    # soluction 2
    Student = namedtuple('Student', ['name','age','sex','email'])
    s = Student('Jim', 16, 'male', 'aa@gmail.com')
    print s
    print s.name
