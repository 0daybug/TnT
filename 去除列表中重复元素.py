#!/usr/bin/env python
#--*-- coding:utf-8 --*--
#去除列表中重复元素
#solution one 使用集合
list1 = ['a','b','a','c']
list(set(list1))

#solution two 使用字典的方式
l1 = ['a','b','a','c']
l2 = {}.fromkeys(l1).keys()
print l2

#用字典 并保持一致
l1 = ['b','c','a','a','c']
l2 = list(set(l1))
l2.sort(key=l1.index)
print l2

#列表推导式
l1 = ['b','c','a','a','c']
l2 = []
[l2.append(i) for i in l1 if not i in l2]
