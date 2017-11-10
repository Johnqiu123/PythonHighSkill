# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 13:51:33 2017

@author: Administrator

问题：如何使用函数装饰器
定义装饰器函数，用它来生成一个在原函数基础添加了新功能的函数，替代原函数

python 装饰器自带的语法堂
@memo 等价于 memo(fibonacci)
"""

def memo(func):
    """装饰器函数"""
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fibonacci(n):
    """菲波那切数列"""
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n -2)

@memo
def climb(n, steps):
    """爬楼梯问题"""
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n - step, steps)
    return count

if __name__ == '__main__':
    print fibonacci(50)
    print climb(10, (1,2,3))
