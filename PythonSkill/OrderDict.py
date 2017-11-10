# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:54:19 2017

@author: Administrator

问题：如何让字典保持有序？
以OrderedDict替代内置字典Dict，依次将选手成绩存入OrderedDict
"""
from collections import OrderedDict
from time import time
from random import randint

if __name__ == '__main__': 
    
    # 直接使用ordereddict
    d = OrderedDict()
    d['Jim'] = (1,35)
    d['Leo'] = (2,37)
    d['Bob'] = (3,40)
    
    for k in d: print k
    
    # 例子
    d = OrderedDict()
    players = list('ABCDEFGH')
    start = time()
    
    for i in range(8):
        raw_input()
        p = players.pop(randint(0, 7 - i))
        end = time()
        print i + 1, p, end -start,
        d[p] = (i + 1, end - start)
    
    print 
    print '-' * 20
    
    for k in d:
        print k,d[k]
    
