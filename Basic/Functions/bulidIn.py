# -*- coding:utf-8 -*-



# isinstance(obj, class_or_tuple)
def my_abc(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    
    if x > 0:
        return x
    else:
        return -x

print(my_abc(-9))
#print(my_abc('xxx'))  # error :  TypeError: bad operand type


# range() : range(stop) -> range object range(start, stop[, step]) -> range object
list1 = [1,2,3,4,5,5,6]
for i in range(10):
    print(i)

for i in range(1,10,2):
    print(i)


# type()
import types

print(type(123)==type(456))         # True
print(type(123)==int)               # True
print(type('abc')==type('123'))     # True
print(type('abc')==str)             # True

def fn():
    pass
type(fn) == types.FunctionType
type(sorted) == types.BuiltinFunctionType
types.LambdaType
types.MethodType
types.GeneratorType

class MyDog(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __len__(self):
        return 10

obj = MyDog('a huang', 2)

# getattr(object, name, default)
print(getattr(obj,'name'))
print(getattr(obj,'sex',None))
# setattr()

# hasattr()
print(hasattr(obj,'name')) # True
print(hasattr(obj,'hhh')) # False



