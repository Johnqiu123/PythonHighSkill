# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 09:35:38 2017

@author: Administrator

问题：如何读写文本文件
【python 2.x】写入文件前对unicode编码，读入文件后对二进制字符串解码
【python 3.x】open函数制定‘t’的文本模式，endcoding指定编码格式
"""

if __name__ =='__main__':
    
    # python2 读写文件
    f = open('Data/py2.txt','w')
    s = u'你好'
    f.write(s.encode('gbk'))
    f.close()
    
    f = open('Data/py2.txt', 'r')
    t = f.read()
    print t.decode('gbk')

   # python3 读写文件
    f = open('Data/py3.txt','wt',encoding = 'utf8')
    f.write('你好，我爱编程')
    f.close()
    
    f = open('Data/py3.txt','rt',encoding = 'utf8')
    s = f.read()
    f.close()
    print(s)