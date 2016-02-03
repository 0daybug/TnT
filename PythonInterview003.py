#!/usr/bin/env python
#coding:utf-8

"""
@staticmethod 和@classmethod
"""

def foo(x):
    print ("executing foo(%s)") % (x)

class A(object):
    def foo(self, x):
        print("executing foo(%s, %s)") % (self, x)

        @classmethod
        def class_foo(cls, x):
            print("executing class_foo(%s, %s)") % (cls, x)

        @staticmethod
        def static_foo(x):
            print("executing static_foo(%s") % x


a = A()

"""
我们来理解一下函数参数里面的self和cls, self和cls是对类或者实例的绑定,
对于一般的函数来说我们调用foo(x), 这个函数是最常用的,它的工作跟任何东西
(类和实例)无关,我们知道在类里每次定义方法的时候都需要绑定这个实例,就是
foo(self, x),为什么要这么做呢?因为实例方法的调用离不开实例,我们需要将实例
自己传递给函数,调用的时候这样的a.foo(x) (其实就是foo(a, x))

类方法一样,只不过它传递的是类而不是实例,A.class_foo(x),注意这边的self和cls可以
替换成别的参数,但是Python的约定是这俩,还是不要改的好

对于静态方法,其实和普通的方法一样,不需要对谁进行绑定,唯一的区别是调用的时候需要使用
a.static_foo(x)或者A.static_foo(x)来调用
"""