# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 08:50:58 2017

@author: Administrator
"""
from multiprocessing import Process, Queue, Pipe
from concurrent.futures import ThreadPoolExecutor

def f(q):
    print 'start'
    print q.get()
    print 'end'

def g(a, b):
    print('g', a, b)
    return a**b

if __name__=='__main__':
    
    # Example 1 了解多进程的使用
    q = Queue()
    Process(target=f, args=(q,)).start()
    q.put(100)
    
    # Example 2 线程池
    executor = ThreadPoolExecutor(3)
    future = executor.submit(g, 2, 4)
    print future.result()
    
