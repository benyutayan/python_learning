'''
Higher-order function

sorted(),
filter(),
map(),
reduce()
  
'''

from functools import reduce

def func1(x):
    return x[0].upper() + x[1:].lower() 

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(func1, L1))
print(L2)


def prod(L=None):
    def func2(x,y):
        return x*y
    return reduce(func2,L)

L = [3, 5, 7, 9]
print(prod(L))

def str2float(str):
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    str1,str2 = str.split('.')
    def func3(x,y):
        return x*10 + y
    def func4(x,y):
        return 0.1*x + y
    return reduce(func3,map(char2num,str1)) + 0.1 * reduce(func4,map(char2num,str2[::-1]))
     
print(str2float('1234.567'))
        
    
# filter
def f1(x):
    return x%2 == 0

list1 = list(filter(f1,[x for x in range(10)]))
print("list 1 = ", list1)



# sorted()

def by_name(t):
    return t[0]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L1 = list(sorted(L,key=lambda x : x[1]))
print(L1)
    


'''
printjs;dlsdksd

'''