# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 21:46:53 2017

@author: Administrator

问题：如何构建xml文档
使用标准库中的xml.etree.ElementTree，构建ElementTree，使用write方法写入文件
"""
import csv
from xml.etree.ElementTree import Element, ElementTree
from Pretty import pretty

def csvToXml(fname):
    with open(fname, 'rb') as f:
        reader = csv.reader(f)
        headers = reader.next()

        root = Element('Data') # 构造根结点
        for row in reader:
            eRow = Element('Row') # 构造子节点
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)

    pretty(root)
    return ElementTree(root)

et = csvToXml('pingan.csv')
et.write('pingan.xml') # 写入xml

