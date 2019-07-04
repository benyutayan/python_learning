
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


  

