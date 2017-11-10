# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:09:53 2017

@author: Administrator

问题：如何使用临时文件
使用标准库中tempfile中的TemporaryFile,NamedTemporaryFile

"""

from tempfile import TemporaryFile, NamedTemporaryFile

if __name__=='__main__':
    
    # 临时文件 无法在系统路径中找到,只能靠对象进行访问
    f = TemporaryFile()
    f.write('abcdef' * 10000)
    f.seek(0)
    print f.read(100)

    # 带名字的临时文件 可以在系统路径中找到
    ntf = NamedTemporaryFile()
    print ntf.name