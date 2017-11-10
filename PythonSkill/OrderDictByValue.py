# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 17:54:59 2017

@author: Administrator

问题：如何根据字典中值的大小，对字典中的项进序
【方法一】利用zip将字典数据转化元组
【方法二】传递sorted函数的key参数
"""
from random import randint
if __name__=='__main__':
    
    score = {x:randint(60,100) for x in 'xyzh'}
    print score
    
    # Solution 1
    result = sorted(zip(score.itervalues(), score.iterkeys()))
    print result
    
    # Solution 2
    result2 = sorted(score.items(), key = lambda x: x[1])
    print result2

