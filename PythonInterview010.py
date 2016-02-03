#coding:utf-8
"""
*args 和**kwargs

用上面两个只是为了方便,并没有强制使用它们

当你不确定你的函数将要传递多少参数的时候,你可以使用*args,例如他可以传递任意数量的参数

"""

def print_everything(*args):
    for count, thing in enumerate(args):
        print('{0}.{1}'.format(count,thing))

print_everything('apple', 'banana', 'cabbage')
"""
0. apple
1. banana
2. cabbage
"""

"""
相似的,**kwargs允许你使用没有事先定义的参数名:
"""
def table_things(**kwargs):
    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))

table_things(apple = 'fruit', cabbage = 'vegetable')

"""
cabbage = vegetable
apple = fruit
"""

"""
你可以混着用,命名参数首先获得参数值,然后所有的其他参数都传递给*args和**kwargs
命名参数在列表的最前端
def table_things(title,**kwargs)

*args和**kwargs可以同时在函数定义中但是*args必须在**kwargs前面
"""

"""
当然你也可以用* 和 **语法 ,只不过传递的参数需吻合
"""