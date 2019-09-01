# -*- coding:utf-8 -*-


from itertools import chain

list1 = chain(range(0,3),range(0,4)) 
print(list1)
#<itertools.chain object at 0x00000250ECA00358>

list2 = list(list1)
print(list2)
#[0, 1, 2, 0, 1, 2, 3]

