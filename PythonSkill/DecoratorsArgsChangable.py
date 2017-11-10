# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 22:19:21 2017

@author: Administrator

问题：如何实现属性可修改的函数装饰器
为包裹函数增添一个函数，用来修改闭包中使用的自由变量。
在python3中，使用nonlocal访问嵌套作用域中的变量引用

注意：如果装饰器中需要带参数，就必须包三层
"""

import time
import logging
from random import randint
def warn(timeout):
    timeout = [timeout] # 从不可变对象变成可变对象
    def decorator(func):
        def wrapper(*args, **kargs):
            start = time.time()
            res = func(*args, **kargs)
            used = time.time() - start
            if used > timeout[0]:
                msg = '"%s": %s > %s' % (func.__name__,used, timeout[0])
                logging.warn(msg)
            return res
        def setTimeout(k):
            # nonlocal timeout
            timeout[0] = k
        wrapper.setTimeout = setTimeout
        return wrapper
    return decorator

@warn(1.5)
def test():
    print('In test')
    while randint(0,1):
        time.sleep(0.5)

if __name__=='__main__':
    for _ in range(30):
        test()
    test.setTimeout(1)
    for _ in range(30):
        test()
            

