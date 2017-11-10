# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:02:40 2017

@author: Administrator

问题：如何使用描述符对实例属性做类型检查
使用描述符来实现需要类型检查的属性：
分别实现__get__,__set__,__delete__方法，在__set__内
使用isinstance函数做类型检查
"""

class Attr(object):
    """定义描述符方法"""
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_
        
    def __get__(self, instance, cls):
        """读取方法"""
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        """设置方法"""
        if not isinstance(value, self.type_):
            raise TypeError('expected an %s' % self.type_)
        
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        """删除方法"""
        del instance.__dict__[self.name]
    
class Person(object):
    name = Attr('name', str)
    age = Attr('age', int)
    height = Attr('height', float)

if __name__ == '__main__':
    p = Person()
    p.name = 'Bob'
    print p.name
    p.age = 1
    print p.age
    print p.__dict__
    del p.age
    print p.__dict__
    
