# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:38:38 2017

@author: Administrator

问题：如何判断字符串a是否以字符串b开头或结尾
使用字符串的str.startswith()和str.endswith()方法
"""

if __name__=='__main__':
    
    s = ['e.py','g.sh','d.java','h.c','f.cpp','a.sh','c.h','b.py']
    
    # 保留py和sh的文件
    res = [name for name in s if name.endswith(('.sh','.py'))]
    print res
