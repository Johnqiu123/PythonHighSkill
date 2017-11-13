# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:29:56 2017

@author: Administrator
"""
from random import randint
data = [randint(1000,10000) for _ in range(1, 10)]
print data
dataSet = {x:[randint(1000,10000) for _ in range(x, 13)] for x in range(1,13)}
print dataSet
print dataSet[1]