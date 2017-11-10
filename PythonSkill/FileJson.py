# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 13:58:13 2017

@author: Administrator

问题：如何读写json数据
使用标准库中的json模块，其中loads，dumps函数可以完成json数据的读写
"""

if __name__ == '__main__':
    
    import json
    
    test = [1,2,'abc',{'b': None, 'a':5, 'c':'abc'}]
    print json.dumps(test)
    
    # None 会被替换null
    test2 = {'b': None, 'a':5, 'c':'abc'}
    print json.dumps(test2)
    
    # 去除压缩后的空格
    print json.dumps(test, separators=[',',':'])
    
    # 压缩后排序
    print json.dumps(test2, sort_keys=True)
    
    # 压缩成文件
    with open('Data/demo.json','wb') as f:
        json.dump(test,f)
    
    # 读取文件
    with open('Data/demo.json','rb') as f:
        print json.load(f)
