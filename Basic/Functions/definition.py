
def my_abs(x):      # x 作为参数，
    if x >= 0:
        return x
    else:
        return -x   #return 后跟想要返回的值

print(my_abs(-0.99))  # 0.99


#空函数,什么也不做，pass
def my_func1(x):
    pass  
  
# 多个参数
def my_func3(x,y):
    return x*x+y*y

result = my_func3(3, 4)
print(result)          #25


#返回值有多个
def my_func2(x):
    return x,x*x

x,y = my_func2(3)
print(x,y)       #3,9

#多个返回值，其实是一个tuple
u = my_func2(3)
print(u)        #(3, 9)



#默认参数, n=2 
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 可变参数, *numbers
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3,4,5))
numbers = [1,2,3,4,5]
print(calc(*numbers))


# 关键字参数, **KW
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('machong',33, city='nanyang')
person('machong',33, city='nanyang',addr='xinye')

d1 = {'city':'nanyang','addr':'xinye'}
person('machong',33,**d1)

# 命名关键字参数, 如果要限制关键字参数的名字，就可以用命名关键字参数.
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person1(name, age, *, city, job):
    print(name, age, city, job)
person1('machong',33, city='nanyang',job='xinye')

def person2(name, age, *args, city, job):
    print(name, age, args, city, job)
person2('machong',33, city='nanyang',job='xinye')


# 参数组合, 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。







  

