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

