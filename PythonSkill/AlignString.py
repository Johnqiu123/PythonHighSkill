# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 20:38:00 2017

@author: Administrator

问题：如何对字符串进行左、右、居中对齐
【方法一】使用字符串的str.ljust()，str.rjust()，str.center()进行左、右、居中对齐
【方法二】使用format()方法，传递类似'<20'，'>20'，'^20'参数完成同样任务
"""

if __name__=='__main__':
    
    d = {
       "lodDist":100.0,
       "SmallCull":0.04,
       "DistCull":500.0,
       "trilinear":40,
       "farclip":477 }
    print d 
    
    # 获取最长的键
    w = max(map(len, d.keys()))
    print w
    
    # 左对齐
    for k in d:
        print k.ljust(w),':',d[k]
    
    val = '<' + str(w)
    for k in d:
        print format(k, val),':',d[k]
    
    # 右对齐
    for k in d:
        print k.rjust(w),':',d[k]
    
    val = '>' + str(w)
    for k in d:
        print format(k, val),':',d[k]
    
    # 中对齐
    for k in d:
        print k.center(w),':',d[k]
    
    val = '^' + str(w)
    for k in d:
        print format(k, val),':',d[k]