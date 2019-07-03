

#output

a = 23
b= 45

print("a+b=",a+b)






#input

name = input("please input\n")
print("name = ",name)

####使用%
print("name = %s"  % name)

i = int(input("输入数字"))
print("i = %d" % i)

#float
f = float(input("输入数字"))
print("f = %f" % f)

#### format(), 墙裂推荐

#如果花括号里面没有序号，则按照出现的顺序进行替换
print('{} {}'.format('xyz',9) )     #xyz 9

#如果花括号里制定了使用参数的序号，则按照序号对应参数进行替换
print('{1} {0} {1} {0}'.format('xyz',9) )    #9 xyz 9 xyz

#使用关键字参数
print('{name} {age}'.format(name='xyz',age=9) )    #xyz 9

#如果需要输出花括号{}本身，可以采用 "{{" 表示 "{" ，用 "}}" 表示 "}"
print('{{ {} {} }}'.format('joe',100))    #{ joe 100 }






