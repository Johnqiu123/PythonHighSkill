# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 13:53:03 2017

@author: Administrator

问题：如何打包所有的xml
调用tarfile方法
"""
import tarfile
import os

def tarXML(tfname):
    print "tarXML"
    tf = tarfile.open(tfname, 'w:gz')
    for fname in os.listdir('Data'):
        print fname
        if fname.endswith('.xml'):
            tf.add('Data/' + fname)
            os.remove('Data/'+ fname)
    tf.close()
    
    if not tf.members:
        os.remove(tfname)

if __name__=="__main__":
    tarXML('test.tgz')
