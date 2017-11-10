# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 14:03:12 2017

@author: Administrator

问题： 如何解析简单的XML文档
使用标准库中xml.etree.ElementTree,其中的parse函数可以解析XML文档
"""
from xml.etree.ElementTree import parse

if __name__=='__main__':
    
    f = open('Data/demo.xml')
    et = parse(f)
    root = et.getroot()
    print root.tag # 标签
    print root.attrib # 属性
    print root.text
    print root.text.strip()
    
    # 打印孩子结点的名字
    for child in root:
        print child.get('name')
    
    print root.find('country')
    print root.findall('country') # 只能找到直接子元素
    
    for e in root.iterfind('country'):
        print e.get('name')
        
    print list(root.iter())
    print list(root.iter('rank'))
    
    # 查找高级用法
    print root.findall('country/*')
    print root.findall('.//rank')
    print root.findall('.//rank/..')
    print root.findall('country[@name]')
    print root.findall('country[rank]')
    print root.findall('country[rank="2"]')
    print root.findall('country[1]')
    print root.findall('country[last()-1]')    
    
