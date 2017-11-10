# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 22:27:38 2017

@author: Administrator

问题：如何在列表、字典、集合中根据条件筛选数据
列表：采用列表解析最快速
字典：iteritems()
集合：类似列表
"""
from timeit import timeit as timeit  
import random

if __name__ == '__main__':  
    data = [1, 5, -3, -2, 6, 0, 9] 
   # 保留正值的数 
   # Solution 1: for loop
    res = []
    for x in data:
        if x >= 0: res.append(x)
    print(res)

   # Solution 2: filter
    print filter(lambda x: x >= 0, data)
#    print timeit('filter(lambda x: x >= 0, [1, 5, -3, -2, 6, 0, 9])')
   
   # Solution 3: 列表解析(只花了一半的时间，最快速)
    print [x for x in data if x >= 0]
#    print timeit('[x for x in [1, 5, -3, -2, 6, 0, 9] if x >= 0]')

   ###########################################
    dataDict = {x : random.randint(60, 100) for x in range(1,21)}
    print dataDict
    
    # 保留等于大于90
    print {k : v for k, v in dataDict.iteritems() if v >= 90}
    
   ##########################################
    dataset = set(data)
    print dataset
    
    # 保留大于等于0的数
    print {x for x in dataset if x >= 0}
    