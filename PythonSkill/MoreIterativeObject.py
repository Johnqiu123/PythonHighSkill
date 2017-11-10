# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:31:41 2017

@author: Administrator

问题：如何在一个for语句中迭代多个可迭代对象？
【并行】使用内置函数zip，它能将多个可迭代对象合并，每次迭代返回一个元组
遇到对象长度不一时，选择最短为主
【串行】使用标准库中的itertools.chain，它能将多个可迭代对象连接
"""
from random import randint 
from itertools import chain

if __name__=='__main__':
    
    # data
    chinese = [randint(60, 100) for _ in range(40)]
    english = [randint(60, 100) for _ in range(50)]
    math = [randint(60, 100) for _ in range(50)]
    
    print chinese
    print english
    print math
    
    # for zip
    total = []
    for c,e,m in zip(chinese, english, math):
        total.append(c + e + m)
    print total
    
    # for chain
    # 获取分数大于90分的数量
    count = 0
    for i in chain(chinese, english, math):
        if i > 90: count += 1
    print count
    
    

