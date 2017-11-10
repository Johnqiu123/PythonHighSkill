# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:57:22 2017

@author: Administrator

问题：如何拆分含有多种分隔符的字符串
【方法一】连续使用是str.split()方法，每次处理一种分隔符号
【方法二】使用正则表达式的re.split()方法，一次性拆分字符串`
"""
def mySplit(s, ds):
    res = [s]
    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t
      
    return [x for x in res if x]

if __name__ == '__main__':
    
    s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
    print mySplit(s, ';,|\t')
    
    # use re
    import re
    print re.split(r'[,;\t|]+', s)
    
    
    