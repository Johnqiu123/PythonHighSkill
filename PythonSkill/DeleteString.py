# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 08:49:24 2017

@author: Administrator

问题：如何去掉字符串中不需要的字符
【方法一】字符串strip()，lstrip()，rstrip()方法去掉字符串两端字符
【方法二】删除单个固定位置的字符，可以使用切片+拼接的方式
【方法三】字符串的replace()方法或正则表达式re.sub()删除任意位置字符
【方法四】字符串translate()方法，可以同时删除多种不同字符
"""
import re
import string

if __name__ == '__main__':
    
    s = "   abc xyz   "
    s1 = "----abc xyz++++"
    s2 = 'abc:123'
    s3 = '\tabc\t123\txyz'
    s4 = '\tabc\t123\txyz\rbdq\r'
    s5 = 'abc1234xyz'
    s6 = 'abc\refg\n123\t'
    s7 = u''
    
    # 去掉字符串两端字符
    print s.strip()
    print s.lstrip()
    print s.rstrip()
    
    print s1.strip('-+')
    print s1.lstrip('-')
    print s1.rstrip('+')
    
    # 去除单个固定位置的字符
    print s2[:3] + s2[4:]
    
    # 删除任意位置字符
    print s3.replace('\t','')
    print re.sub('[\t\r]', '', s4)
    
    # 删除多种不同字符
    table = string.maketrans('abcxyz','xyzabc') # 建立映射表
    print s5.translate(table)
    
    print s6.translate(None,'\r\n\t')
    
    # 去除unicode上的音调
    print s7.translate(dict.fromkeys([0x301,0x030c,0x0304,0x0300]))
    