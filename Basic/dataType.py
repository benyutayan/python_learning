
### list
L1 = []                        #空
l2 = [1,23,45,7]               #
L3 = [1,'b','ddd',True]        #list元素可以是不同类型的
L4 = [1,'t',['ac','bn'],9,90]  #list元素可以是一个list
#追加元素到末尾，append()
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



### set , 一组key的集合，但不存储value
#要创建一个set，需要提供一个list作为输入集合：

#add(key)方法可以添加元素到set中,
#remove(key)方法可以删除元素
