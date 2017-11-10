# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 15:15:31 2017

@author: Administrator

问题：如何设置文件的缓冲
【全缓冲】open函数的buffering设置为大于1的整数n，n为缓冲区大小
【行缓冲】open函数的buffering设置为1，遇到‘\n’写入
【无缓冲】open函数的buffering设置为0
"""
if __name__=='__main__':
    
    # 正常文件缓冲
    f = open('Data\demo.txt','w')
    f.write('abc')
    f.write('+' * 4093)
    f.write('-')
    f.write('*' * 4095)
    f.write('x')
    f.close()
    
    # 全缓冲 设置buffering
    f = open('Data\demo.txt','w', buffering=2048)
    f.write('+' * 1024)
    f.write('+' * 1023)
    f.write('-' * 2)
    f.close()
    
    # 行缓冲 设置buffering=1，遇到‘\n’写入
    f = open('Data\demo.txt','w', buffering=2048)
    f.write('abcd')
    f.write('1234')
    f.write('\n')
    f.write('xyz\n')
    
    # 无缓冲 设置buffering=0
    f = open('Data\demo.txt','w', buffering=0)
    f.write('abcd')
    
