# -*- coding:utf-8 -*-

'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

'''

from functools import reduce

def fn(x, y):
    return 10 * x + y

list1 = reduce(fn,[1,3,5,7,9])
print(list1)