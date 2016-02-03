#coding:utf-8
"""
类变量与实例变量
"""
class Person:
    name = "aaa"

p1 = Person()
p2 = Person()
p1.name = "bbb"

print (p1.name) #bbb
print (p2.name) #aaa
print (Person.name) #aaa

"""
类变量就是提供类使用的变量,实例变量就是提供实例使用的

p1.name="bbb" 是实例调用了类变量,其实这个和上面第一个问题是一样的,就是函数传递参数的问题
p1.name一开始是指向的类变量name="aaa" 但是在实例的作用域的变量引用改变了,就变成了一个
实例变量,self.name不再引用Person的变量name了
"""

#eg2
class Person:
    name = []

p1 = Person()
p2 = Person()
p1.name.append(1)

print(p1.name) #[1]
print(p2.name) #[1]
print(Person.name) #[1]