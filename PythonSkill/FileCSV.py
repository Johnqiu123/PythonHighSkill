# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 13:29:07 2017

@author: Administrator

问题：如何读写csv数据
使用标准库中的csv模块，可以使用其中reader和writer完成csv文件读写
"""

import csv

with open('xx.csv','rb') as rf:
    reader = csv.reader(rf)
    with open('xx.csv','wb') as wf:
        writer = csv.writer(wf)
        headers = reader.next()
        writer.writerow(headers)
        for row in reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) >= 500000:
                writer.writerow(row)
print 'end'



