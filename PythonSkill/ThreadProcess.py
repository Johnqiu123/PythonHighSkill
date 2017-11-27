# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 09:04:05 2017

@author: Administrator

问题：如何使用多进程
使用标准库中multiprocessing.Process,它可以启动子进程

题目：在n位的整数中，例如153可以满足1^3 + 5^3 + 3^3 = 153，这样的数称之为Armstrong数。
将所有的Armstrong数按小到大排序，试写出一程序找出n位数以下的所有Armstrong数

小范围的时候多线程快
大范围的时候多进程快
"""
from threading import Thread
from multiprocessing import Process

def isArmstrong(n):
    """基本Armstrong算法"""
    a, t=[],n
    while t > 0:
        a.append(t % 10)
        t /= 10
    k = len(a)
    return sum(x ** k for x in a) == n

def findArmstrong(a, b):
    print a, b 
    res = [k for k in xrange(a,b) if isArmstrong(k)]
    print '%s - %s: %s' % (a, b, res)

def findByThread(*argslist):
    workers = []
    for args in argslist:
        worker = Thread(target=findArmstrong, args=args)
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

def findByProcess(*argslist):
    workers = []
    for args in argslist:
        worker = Process(target=findArmstrong, args=args)
        workers.append(worker)
        worker.start()
    
    for worker in workers:
        worker.join()

if __name__ == '__main__':
    import time
    start = time.time()
#    findByProcess((2000,2500),(2500, 3000)) # 多进程
    findByThread((2000,2500),(2500, 3000)) # 多线程
    print time.time() - start

