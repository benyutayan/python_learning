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
print(my_abc('xxx'))  # error :  TypeError: bad operand type



