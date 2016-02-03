"""
Python中单下划线和双下划线
"""

class MyClass():
    def __init__(self):
        self.__superprivate = "hello"
        self._semiprivate = ", world"

mc = MyClass()

print(mc.__superprivate) #error! error! error! 重要的事情说三遍
print(mc._semiprivate) #, world
print(mc.__dict__) #{'_MyClass__superprivate':'hello', '_semprivate': ', world'}

"""
__foo__: 一种约定,Python内部的名字,用来区别其他用户自定义的命名,防止冲突

_foo:一种约定,用来指定变量私有,程序员用来指定私有变量的一种方式

__foo:这个有真正的意义:解析器用_classname__foo来代替名字,以区别和其他类相同的命名
"""

