#创建字典的方法

#1.直接创建
dict = {'name':'earth', 'port':'80'}

#2.工厂方法
items = [('name', 'earth'), ('port', '80')]
dict2 = dict(items)
dict1 = dict([('name', 'earth'), ('port', '80')])

#3.fromkeys()方法
dict1 = {}.fromkeys(('x', 'y'), -1)
#dict1 : {'x':-1, 'y':-1}
dict2 = {}.fromkeys(('x', 'y'))
#dict2 : {'x':None, 'y':None}
