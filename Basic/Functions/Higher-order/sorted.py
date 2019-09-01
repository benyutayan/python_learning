# -*- coding:utf-8 -*-

# sorted()

def by_name(t):
    return t[0]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L1 = list(sorted(L,key=lambda x : x[1]))
print(L1)

