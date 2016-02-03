#!/usr/bin/env python
#coding:utf-8
"""
Python的函数参数传递

#eg 1
a = 1
def fun(a):
    a = 2

fun(a)
print (a)

#最后输出 1
"""

#eg2

a = []
def fun(a):
    a.append(1)

fun(a)
print (a)

#输出 [1]

"""
conclusion:
所有变量可以理解为内存中一个对象的引用
类型是属于对象的,而不是变量!
类型是属于对象的,而不是变量!
类型是属于对象的,而不是变量!
重要的事情说三遍

对象有两种,"可以更改(mutable)"对象 与 "不可以更改immutable"对象

Python中 strings,tuples和numbers是不可更改的对象
         list,dict则是可以更改的

当一个引用传递给函数的时候,函数自动复制一份引用,这个函数里的引用和外边的引用无关, eg1里面的函数把引用
指向了一个不可变对象,当函数返回的时候,外面的引用没有发生任何变化,所以在执行print (a)的时候返回结果还是1
那么相反 eg2中是一个list, 函数的引用指向可变对象,那它的操作就和定位指针地址一样,在内存中修改了
"""