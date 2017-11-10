# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:49:41 2017

@author: Administrator

问题：如何调整字符串中文本的格式
使用正则表达式re.sub()方法做字符串替换，利用正则表达式的捕获组，
捕获每个部分内容，在替换字符串中调整各个捕获组的顺序
"""
import re

if __name__ == '__main__':
    
    s = '2016-02-03 dddd 2016-01-02'
    print s
    
    # 检测出日期，然后调整格式
    result = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', s)
    print result
    
    # 增加标签
    result2 = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', s)
    print result2
    

