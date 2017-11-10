# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 20:13:55 2017

@author: Administrator

问题：如何将多个小字符串拼接成一个大的字符串
【方法一】迭代列表，连续使用“+”操作依次拼接每一个字符串
会带来额外的开销
【方法二】使用str.join()方法，更加快速的拼接列表中所有字符串
"""

if __name__ == '__main__':
    args = ["<0112>","<32>","<1024X768>","<60>","<1>","<100.0>","<500.0>"]
    
    # Soluntion 1
    s = ''
    for arg in args:
        s += arg # 生成一个新的字符串
    print s
    
   # Soluntion 2
    s2 = ''.join(args)
    print s2

   # 连接数字和字符串
    vals = ["abc",34,45,"xyz"]
    s3 = ''.join(str(val) for val in vals) # 使用生成器代替列表
    print s3
    