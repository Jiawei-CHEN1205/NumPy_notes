# ***** numpy 学习笔记day1 from runoob.com 
# ***** author： WendyCHEN
# from numpy import *
import numpy as np
# array = np.eye(4) # eye() 生成对角矩阵
# print(array)
# a = np.array([1, 2, 3, 4, 5], ndmin =  3)  # 最小维度
# print (a)

# dt = np.dtype([('age',np.int8)]) 
# a = np.array([(10,),(20,),(30,)], dtype = dt) 
# print(a['age'])
# print(a[2])

# student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
# astu = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
# print(astu)



# matrix = [[1,2,3,4],
# [5,6,7,8],
# [9,10,11,12],] # 3*4 matrix
# # 转置矩阵
# transposed_list1 = [[row[i] for row in matrix] for i in range(4)] # 4是因为每个行row有4个元素 row[0]到row[3]
# print(transposed_list1)


# # tuple 元组 可以嵌套
# t = 'hello', 22.5 , 8765
# u = t, (1,4,7)
# print(t)
# print(u) # output: (('hello', 22.5, 8765), (1, 4, 7)) 



# a = np.arange(24)  # arange生成 0-23的一维数组 
# # 使用 arange 函数创建数值范围 并返回 ndarray 对象
# print (a.ndim)             # a 现只有一个维度
# print(a)
# # 现在调整其大小
# b = a.reshape(3,4,2)  # b 现在拥有三个维度 24=3*4*2
# print (b.ndim)
# print(b)
# print(b.shape) # (3, 4, 2)

# a = np.array([[1,2,3],
# [4,5,6]])  
# print (a.shape) # (2, 3) 
# # ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性(秩)。比如，一个二维数组，其维度表示"行数"和"列数"
# print(a)


# # ndarray.reshape 通常返回的是非拷贝副本，即改变返回后数组的元素，原数组对应元素的值也会改变。
# # copy() 是拷贝副本 改变y 不影响x 见下例子：
# x = np.array([1,2,3,4,5]) 
# y = x.copy() 
# # print (x.flags)
# # print (y.flags)
# y[0] = 102
# print(y)
# print(x)
# # [102   2   3   4   5]
# # [1 2 3 4 5]

# z = np.zeros([2,2], dtype = [('x', 'f4'), ('y', 'i4')])  
# # z = np.zeros((2,2), dtype = [('x', 'f4'), ('y', 'i4')])  # [2,2]处，用方括号和圆括号均可
# print(z)
# print(z['x'])
# print(z['y'])

# # 动态数组
# # buffer 是字符串的时候，Python3 默认 str 是 Unicode 类型，
# # 所以要转成 bytestring 在原 str 前加上 b。
# s =  b'Hello World'  # b是字符串改二进制字符串 必须写b 在python3.x中
# a = np.frombuffer(s, dtype =  'S1')  
# print (a)


# # 使用 range 函数创建列表对象  
# list=range(5)
# it=iter(list) #貌似 inter()函数的功能是，使一个有序序列变成可迭代对象interable
# # fromiter 使用迭代器创建 ndarray 
# x=np.fromiter(it, dtype=float)
# print(x)


# xp = np.arange(4.2 , 13.8 , 0.3) 
# print(xp)
# xp2 = np.arange(1,9,2) #不包含stop
# print(xp2)

# a = np.linspace(0,0.9,10,retstep= True) #包含stop # 10个数，其实是九个间距
# print(a)

# linspace()是等差数列； logspace()是等比数列
log1 = np.logspace(1,5,5) #默认是以10为底
print(log1)

log2 = np.logspace(2,9,8,base = 2)
print(log2)
# 发现一个技巧，num的数量的确定，只要满足stop - start + 1即可


a2 = np.array([[1,2,3,18],[4,5,6,23],[7,8,9,77]])
print(a2.ndim) # 2 dimension
print(a2.shape) # (3,4)


# 切片还可以包括省略号 …，来使选择元组的长度与数组的维度相同。
# 如果在行位置使用省略号，它将返回包含行中元素的 ndarray
a3 = np.array([[1,2,3,78,99],[3,999,5,10,12],[4,25,6,67,89]])  
print (a3[...,3])   # 每一行的第4列元素 都取出来 [78 10 67]
print (a3[2,...])   # 第3个元素 [4,25,6,67,89]
print (a3[...,2:])  # 每一行的第3列及剩下的所有列元素


# 高级索引
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]]) 
print(x)

# 方法1：
print ('\n')
rows = np.array([[0,0],[3,3]]) 
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols]  
print  ('方法1：这个数组的四个角元素是：')
print (y)

# 方法2：
z = x[[0,0,3,3], [0,2,0,2]]
print('方法2：取对角线4个元素')
print(z) # z 是一行的，不是按照2*2出现的四个对角元素
rt = z.reshape(2,2)
print(rt) # 对z reshape即可


if y.all() == rt.all(): #y和rt是一样的！
    print('nice!')
    pass
else:
    print('sad!')
















