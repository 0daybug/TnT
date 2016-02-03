#!/usr/bin/env python
#coding:utf-8

"""
Python 中元类(metaclass)

非常不常用,但是像ORM着红复杂的结构还是会需要使用

元类让你来定义某些类是如何被创建出来的,从根本上说,赋予你如何创建类的控制权
(你甚至不用去想类实例层面上的东西)
你可以将元类想成一个类中类,或是一个类,它的实例是其他的类,实际上,当你在创建一个
新类的时候,你就是在使用默认的元类,它是一个对象(对传统的类来说,他们的元类是一个(type.ClassType))


When do we use metaclass?
 元类一般用于出创建类,在执行类定义时,解释器必须要知道这个类的正确元类,
 解释器会先寻找__metaclass__ ,如果此属性存在,就将这个属性赋值给此类作为它的元类,如果
 没有找到,则会向上查找父类中的__metaclass__.所有新风格的类没有任何父类,会从
 对象或者类型中继承(type(object)当然是类型)

元类通常传递三个参数(到构造器):类名,从基类继承数据的元祖和(类的)属性字典
"""

#example one

from time import ctime
print ('************')
print ('\tMetaclass declaration first.')

class MetaC(type):
    def __init__(cls, name, bases, attrd):
        super(MetaC, cls).__init__(name, bases, attrd)
        print ('*** Created class %r at %s') % (name, ctime())

print ('\t Class "Foo" declaration next.')

class Foo(object):
    __metaclass__ = MetaC
    def __init__(self):
        print ('*** Instantiated class %r at: %s') % (self.__class__.__name__, ctime())

print('\t Class "Foo" instantiation next.')

f = Foo()
print('\t DONE')


