#lambda 


def sum(x,y):
    return x+y
  
print(sum(5,6))  #11

g = lambda x,y : x+y

print(g(5,6))  #11


#lambda 作为返回值
def make_incrementor(n):
    return lambda x : x + n
  
g = make_incrementor(42)
print(g)  #<function make_incrementor.<locals>.<lambda> at 0x000001BC68323620>

print(g(12))   #54

