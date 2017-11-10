# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 21:19:13 2017

@author: Administrator
"""

def alterSeq(n, A):
    i = 1
    maxLen = 1
    temp = 0
    tempLen = 0
    last = A[0]
    begin = 0
    while n > i:
        temp = A[i]
        if temp != last:
            last = temp
        else:
            tempLen = i - begin
            if tempLen > maxLen : 
                maxLen = tempLen
            begin = i
        i += 1
    tempLen = i - begin
    if tempLen > maxLen : 
        maxLen = tempLen
    print(maxLen)

if __name__ == '__main__':
    n = int(raw_input())
    A = [int(i) for i in list(raw_input())]
    alterSeq(n,A)
        