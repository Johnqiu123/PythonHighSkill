# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:33:52 2017

@author: Administrator

问题: 如何快速找到多个字典中的公共键？
1.使用字典的viewkeys()方法，得到一个字典keys的集合
2.使用map函数，得到所有字典的keys的集合
3.使用reduce函数，取所有字典的keys的集合的交集

"""
from random import randint,sample

if __name__ == '__main__': 
    
    # 随机产生相关键值对
    s1 = {x: randint(1,4) for x in sample('abcdefg', randint(3,6))}
    s2 = {x: randint(1,4) for x in sample('abcdefg', randint(3,6))}
    s3 = {x: randint(1,4) for x in sample('abcdefg', randint(3,6))}
    
    print s1,s2,s3
    
    # Solution 1: for loop
    res = []
    for k in s1:
        if k in s2 and k in s3:
            res.append(k)
    print(res)
    
    # Solution2: viewkeys()方法求交集
    val = s1.viewkeys() & s2.viewkeys() & s3.viewkeys()
    print(val) 
    
    # Solution3: 使用map、reduce、viewkeys方法
    result = reduce(lambda a,b: a & b, map(dict.viewkeys, [s1,s2,s3]))
    print(result)
       
