# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:36:27 2017

@author: Administrator

问题：如何进行反向迭代以及如何实现反向迭代？
实现反向迭代协议的_reversed_方法，它返回一个反向迭代器
"""

class FloatRange:
    
    def __init__(self, start, end, step = 0.1):
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t   # 直接返回值，然后下次执行从这里开始
            t += self.step
    
    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

if __name__ == '__main__':
    
    # 正向迭代
    for x in FloatRange(1.0, 4.0, 0.5):
        print x
    
    print '-' * 20
    # 反向迭代
    for x in reversed(FloatRange(1.0, 4.0, 0.5)):
        print x