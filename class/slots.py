# -*- coding:utf-8 -*-

'''
__slots__变量，来限制该class实例能添加的属性：  仅对当前类实例起作用，对继承的子类是不起作用的：
除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
'''

class Student(object):
    __slots__ = ('name','age')

s = Student()

s.name = 'shabi'
#s.stage = 12

class Student1(Student):
    pass

s1 = Student1()
s1.stage = 12


