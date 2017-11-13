# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:22:42 2017

@author: Administrator
"""
import xlwt
from random import randint
class generateDAU(object):
    def __init__(self, fname):
        self.fname = fname
    
    def createExcel(self):
        dataSet = {x:[randint(1000,10000) for _ in range(x, 13)] for x in range(1,13)}
        wbook = xlwt.Workbook(encoding = 'utf-8') # create workbook
        wsheet = wbook.add_sheet('dau')
        
        for i in range(1, 13):
            wsheet.write(0, i, str(i)+' mon')
        
        for k in dataSet:
            wsheet.write(k, 0, str(k)+' mon')
            for j in range(0, len(dataSet[k])):
                wsheet.write(k, j + k, dataSet[k][j])
        wbook.save(self.fname)

if __name__=='__main__':
    genDau = generateDAU('Data/DAUTest.xls')
    genDau.createExcel()
            
        
        
        
        
        