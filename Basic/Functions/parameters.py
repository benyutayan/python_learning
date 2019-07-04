
##默认参数， 默认参数必须指向不变对象！ 
def my_func1(x,y=2):
    return x + y

result = my_func1(3)
print(result)    #5

result = my_func1(3，7)
print(result)    #10



##可变参数， 允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

 
sum = calc(1,2,3)
print(sum)

#有list或tuple时，可在其前边加*
L1 = [1,2,3,4,5]
print('l1 = {}'.format(calc(*L1)))


##关键字参数，允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
#当你想传入更多参数时，  
person("calke", 11, city="nanjing")        #name: calke age: 11 other: {'city': 'nanjing'}
person("calke", 11, city="nanjing",school="tianjindaxue")  
#name: calke age: 11 other: {'city': 'nanjing', 'school': 'tianjindaxue'}

#简化写法
dict1 = {'city': 'nanjing', 'school': 'tianjindaxue'}
person("calke", 11, **dict1)  
#name: calke age: 11 other: {'city': 'nanjing', 'school': 'tianjindaxue'}



##命名关键字参数
def person(name, age, *, city, job):
    print('name:', name, 'age:', age, 'city:',city,'job:',job) 
    
person("calke", 11, city="guangzhou",job="worker")

#当函数定义中已经有一个可变参数，后面跟着的命名关键字参数就不再需要*了
def person2(name, age, *number, city, job):
    sum = 0
    for i in number:
        sum = sum + i
    print(sum)
    print('name:', name, 'age:', age, 'city:',city,'job:',job) 
person("zhangliang", 13,1,23,34,city="jiangshan",job="harkd")


##参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

    
#调用上述函数时，你可以
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
#a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
#a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

    


