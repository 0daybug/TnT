#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
台阶问题/斐波那契
一只青蛙一次可以跳一节台阶，也可以跳上2级，求该青蛙跳上n阶台阶总共有多少种跳法？
"""
#solution one
fib = lambda n:1 if n <=2 else fib(n - 1) + fib(n - 2)

#solution two
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
            return cache(args)
    return wrap

@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i - 1) + fib(i - 2)
