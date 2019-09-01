
### list
L1 = []                        #空
l2 = [1,23,45,7]               #
L3 = [1,'b','ddd',True]        #list元素可以是不同类型的
L4 = [1,'t',['ac','bn'],9,90]  #list元素可以是一个list

#用len()函数可以获得list元素的个数
print("length of L4 : ",len(L4))
#追加元素到末尾，append()
L4.append(66)
print("append()", L4)
#多个list相加
L4 = L4 + l2
print(L4)
#把元素插入到指定的位置,insert(index,value)
#要删除list末尾的元素，用pop()方法：
#要删除指定位置的元素，用pop(i)方法

### tuple ，tuple一旦初始化就不能修改
t1 = ()                        #空
t2 = (1,)                      #只有1个元素的tuple,要加一个逗号，
t3 = ('a', 'b', ['A', 'B'])



###dict , 用键-值（key-value）存储, dict的key必须是不可变对象
d = {'Name':'lishu', 'age': 75, 'city': 'jiangnanxi'}

#in判断key是否存在
if 'job' in d:
    print(True)
    
#dict提供的get()方法,判断key是否存在. get(key, default)
d.get('job')     #None
d.get('job',-1)  #-1

#要删除一个key，用pop(key)方法
d.pop('age',0)



### set , 一组key的集合，但不存储value
#要创建一个set，需要提供一个list作为输入集合：
list1 = [1,2,3,4,4,4,4,4,4]
s1 = set(list1)
print(s1)

#add(key)方法可以添加元素到set中,
s1.add('a')
print(s1)
#remove(key)方法可以删除元素
s1.remove(1)
print(s1)

s2 = set(['b','c','d'])
print(len(s2))

#并集
s3 = s1 & s2  
s4 = s1.intersection(s2)
print(s3,':', s4)

#交集
print(s1 | s2)
print(s1.union(s2))


#差集
print(s1 - s2)
print(s1.difference(s2))


#包含关系
'''
set.isdisjoint(s)：判断两个集合是不是不相交
set.issuperset(s)：判断集合是不是包含其他集合，等同于a>=b 
set.issubset(s)：判断集合是不是被其他集合包含，等同于a<=b 
'''
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))



#集合可以转换为list，tuple以及str
list1 = list(s1)
tu = tuple(s1)
string1 = str(s1)

#不变集合
a = frozenset('hello')
print("type of a : ",type(a))
print(a)
