# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 15:43:35 2017

@author: Administrator

问题：如何将文件映射到内存？
使用标准库中mmap模块的mmap()函数，它需要一个打开的文件描述符作为参数
"""
import mmap
if __name__=='__main__':
    
    f = open('Data/demo.bin','w+b')
    print f.fileno() # 创建文件标识符
    m = mmap.mmap(f.fileno(),0,access = mmap.ACCESS_WRITE)
    print type(m)
    print m[0]
    m[0] = '\x88'
    m[4:8] = '\xff' * 4
    
    m = mmap.mmap(f.fileno(), mmap.PAGESIZE * 8, access=mmap.ACCESS_WRITE, offset = mmap.PAGESIZE * 4)
    m[:0x1000] = '\xaa' * 0x1000
