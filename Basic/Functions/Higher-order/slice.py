# -*- coding:utf-8 -*-

list1 = [n for n in range(10) ]
print(list1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 取前3个元素
print(list1[:3])   # [0, 1, 2]

# 从索引1开始，取出2个元素出来
print(list1[1:3])  # [1, 2]

# 倒数第一个元素的索引是-1
print(list1[-1])   # 9

print(list1[-2:-1])  #[8]

print(list1[:-1])   #[0, 1, 2, 3, 4, 5, 6, 7, 8]

#print(list1[])

# 复制一个list
print(list1[:])   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 反转一个list
print(list1[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]



