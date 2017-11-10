# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 09:35:31 2017

@author: Administrator

问题：如何统计序列中元素的出现频度
将序列传入Counter的构造器，得到Counter对象是元素频度的字典
Counter.most_common(n)方法得到频度最高的n个元素的列表
"""
from random import randint
from collections import Counter

if __name__=='__main__':
    
    data = [randint(0,20) for _ in range(30)]
    print data
    c = Counter(data) # 定义counter对象
    print c

    res = c.most_common(3) # 返回频度最高的3个元素的列表
    print res
