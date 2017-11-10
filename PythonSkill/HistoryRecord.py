# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 06:59:06 2017

@author: Administrator

问题：如何实现用户的历史记录功能
使用容量为n的队列存储历史记录
使用标准库collections中的deque，它是一个双端循环队列
程序退出前，可以使用pickle将队列对象存入文件，再次运行程序时将其导入
"""
from random import randint
from collections import deque
import pickle

def guess(k,N):
    if k == N:
        print 'right'
        return True
    if k < N:
        print '%s is less than N' % k
    else:
        print '%s is greater than N' % k
    return False
    
if __name__ == '__main__':
    # 设计一个猜数字的游戏
    history = deque([], 5)
    N = randint(0,100)
    
    while True:
        line = raw_input("please input a number:")
        if line.isdigit():
            k = int(line)
            history.append(k)
            if guess(k, N):
                break
        elif line == 'history' or line == 'h?':
            print list(history)
    
    # store history
    filename = "Data/history.txt"
    pickle.dump(history, open(filename,'w'))
    result = pickle.load(open(filename))
    print result
            
            
