'''
Iterable
Iterator
''''

### Iterable 可迭代对象
'''
可以直接作用于for循环的对象统称为可迭代对象,如list、tuple、dict、set、str , generator

'''
#isinstance()判断一个对象是否是Iterable对象

from collections.abc import Iterable
a = []
print(isinstance(a, Iterable))  # True
b = (x for x in range(5))
print(isinstance(b, Iterable))  # True



### Iterator , except : StopIteration 
'''
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
'''
from collections.abc import Iterator
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
print(next(b)  # 1




