#!/usr/bin/env python
# encoding: utf-8
import math
def is_prime(n):
    list_num = []
    for i in range(2, n):
        for num in range(2, int(math.sqrt(n)) + 1):
            if i % num == 0 and i != num:
                break
            elif i % num != 0 and num == (int(math.sqrt(n))):
                list_num.append(i)
    return list_num

n = 10
while n <= 1000:
    list_prime = []
    list_prime = is_prime(n)
    n += 1

print list_prime

