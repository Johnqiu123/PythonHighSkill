# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 20:12:49 2017

@author: Administrator

问题：如何为被装饰的函数保存元数据
使用标准库functools中的装饰器wraps装饰内部包裹函数，可以制定将原函数的某些属性，更新
到包裹函数上面

关键方法：update_wrapper
"""
from functools import update_wrapper,wraps,WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES

def mydecorator(func):
    @wraps(func) # 方法三，装饰器
    def wrapper(*args, **kargs):
        """wrapper function"""
        print "In wrapper"
        func(*args, **kargs)
    # 方法1：直接写出来
#    update_wrapper(wrapper, func, ('__name__','__doc__'),('__dict__',))
    # 方法2：默认参数
#    update_wrapper(wrapper, func)
    return wrapper

@mydecorator
def example():
    """example function"""
    print "In example"

if __name__=='__main__':
    print example.__name__
    print example.__doc__
    print example.__dict__
    print WRAPPER_ASSIGNMENTS
    print WRAPPER_UPDATES