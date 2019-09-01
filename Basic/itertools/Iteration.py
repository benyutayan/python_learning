# -*- coding:utf-8 -*-

from collections.abc import Iterable, Iterator

### Iterable 可迭代对象
'''
可以直接作用于for循环的对象统称为可迭代对象,如list、tuple、dict、set、str , generator
#isinstance()判断一个对象是否是Iterable对象
'''
print(isinstance('12',str))  # True



### Iterator , except : StopIteration 
'''
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
'''
a = []
print(isinstance(a, Iterator))  # False
b = (x for x in range(5))
print(isinstance(b, Iterator))  # True


### iter() ,
'''
把Iterable变成Iterator可以使用iter()函数
'''
a = [1,2,3,4,5,6]
b = iter(a)
print(isinstance(b,Iterator))   # True
print(next(b))  # 1


# items()
dict1 = {'name':'zhangliang','age':123}
for k , v in dict1.items():
    print(k,v)


# enumerate()
for index,value in enumerate(range(10)):
    print(index, value)
