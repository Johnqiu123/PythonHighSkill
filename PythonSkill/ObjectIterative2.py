# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:17:55 2017

@author: Administrator

问题：如何使用生成器函数构造可迭代对象？
将该类的__iter__方法实现生成器函数，每次yield返回一个值
"""

class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def isPrimeNum(self, k):
        """judge a num whether is prime"""
        if k < 2:
            return False
        
        for i in xrange(2, k):
            if k % i == 0:
                return False
        
        return True
    
    def __iter__(self):
        """use iter method"""
        for k in xrange(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k

if __name__ == '__main__':
    
    for i in PrimeNumbers(1, 100):
        print i
