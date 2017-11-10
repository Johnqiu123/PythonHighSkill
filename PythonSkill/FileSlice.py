# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:50:41 2017

@author: Administrator

问题：如何对迭代器做切片操作
使用标准表中的itertools.islice,它能返回一个迭代对象切片的生成器
注意这里会对原来的迭代器造成消耗
"""
from itertools import islice
if __name__=='__main__':
    
    filename = 'Data/history.txt'
    f = open(filename)
    
    # 中间切片
    for i in islice(f, 3, 6):
        print i
    
    # 结尾切片
    for i in islice(f, 10):
        print i
    
    # 开头切片
    for i in islice(f, 6, None):
        print i