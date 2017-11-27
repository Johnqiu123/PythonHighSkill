# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 14:12:54 2017

@author: Administrator

问题：如何访问文件的状态
1)标准库中os模块下的三个系统调用stat，fstat，lstat获取文件状态
2)标准库中os.path下一些函数，使用起来更加简洁
"""
import os
import stat

print os.stat('Data/test.txt')
print os.lstat('Data/test.txt')
f = open('Data/test.txt')
print os.fstat(f.fileno())

"""分析文件的状态"""
s = os.stat('Data/test.txt')
print s.st_mode
print bin(s.st_mode) # 转换成二进制
print stat.S_ISDIR(s.st_mode) # 是否是文件夹
print stat.S_ISREG(s.st_mode) # 是否是普通文件
print s.st_mode & stat.S_IRUSR # 检验文件读的权限，大于0即可
print s.st_mode & stat.S_IXUSR # 检验文件的执行权限

"""分析文件的时间"""
import time
t = s.st_atime
print s.st_atime
print time.localtime(t) # 转换成当地时间

print s.st_size # 文件的大小

"""使用os.path的方法"""
print os.path.isdir('Data/test.txt')
print os.path.islink('Data/test.txt')
print os.path.isfile('Data/test.txt')
print os.path.getatime('Data/test.txt')
print os.path.getsize('Data/test.txt')
