#!/usr/bin/env python
# encoding: utf-8

#输出100~1的数字
list1 = []
for i in range(1,101):
    list1.append(i)

list1.reverse()

print list1

#解法2

j = 100
while j > 0:
    print j
    j -= 1
