# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 21:36:31 2017

@author: Administrator

问题：如何定义带参数的装饰器
带参数的装饰器，也就是根据参数定制化一个装饰器，可以看成生产装饰器的工厂。
每次调用typeassert，返回一个特定的装饰器，然后用它去修饰其他函数

提取函数签名：inspect.signature()
python2里面，inspect没有signature方法，只有python3有

从funcsigs 里面导入signature即可
"""

from funcsigs import signature

def typeassert(*ty_args, **ty_kargs):
    def decorator(func):
        # func -> a,b
        # d = {'a':int, 'b':str}
        sig = signature(func)
        btypes = sig.bind_partial(*ty_args, **ty_kargs).arguments # 获得默认参数类型字典
        def wrapper(*args, **kargs):
            # arg in d, instance(arg, d[arg])
            for name, obj in sig.bind(*args, **kargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError('"%s" must be "%s"' % (name, btypes[name]))
            return func(*args, **kargs)
        return wrapper
    return decorator

@typeassert(int, str, list)
def f(a,b,c):
    print(a,b,c)

if __name__ == '__main__':
    f(1,'abc',[1,2,3])
    f(1,2,3)