# *****  numpy 笔记day2
# ***** author： WendyCHEN
import numpy as np


#  isNaN() 函数 用于检查其参数是否是非数字值。如果参数值为 NaN 或字符串、对象、undefined等非数字值则返回 true,否则返回 false
a1 = np.array([np.nan, 1,2,6,np.nan, 777,12])
print(a1[~np.isnan(a1)]) # ~取反
# print(a1[np.isnan(a1)])
# print(np.nan) # 非数值符号 nan


a2 = np.array([1,  2+6j,  5,  3.5+5j])  
print (a2[np.iscomplex(a2)])

# 花式索引 例如使用一维数组、二维数组作为索引
# 花式索引跟切片不一样，它总是将数据复制到新数组中
x = np.arange(32).reshape((8,4)) # x 是二维的
print(x,'\n索引后：',x.ndim)
print(x[[4,2,1,7]]) # 4 2 1 7行
print(x[[1,3,4,5],[2,1,2,3]]) # 位置(1,2) (3,1) (4,2) (5,3)的元素 

# x[np.ix_([1,5,7,2],[0,3,1,2])] 这句话会输出一个4*4的矩阵
# np.xi_ 中输入两个列表，则第一个列表存的是待提取元素的行标，第二个列表存的是待提取元素的列标，
# 第一个列表中的每个元素都会遍历第二个列表中的每个值，构成新矩阵的一行元素。
# x[1,0] x[1,3] x[1,1] x[1,2]
# x[5,0] x[5,3] x[5,1] x[5,2]
# x[7,0] x[7,3] x[7,1] x[7,2]
# x[2,0] x[2,3] x[2,1] x[2,2]
x2=np.arange(32).reshape((8,4))
print('\n')
print (x2[np.ix_([1,5,7,2],[0,3,1,2])])

b = np.array([1,2,3])
bb = np.tile(b, (4, 1))  # 重复 b 的各个维度
print(bb)

# broadcast 广播
a3 = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
print(a3 + b) # 4x3的二维数组与长为3的一维数组相加，等效于把数组b在二维上重复4次再运算
print('\n')
print(a3 + bb) # 与前面a3 + b效果相同

bbb = np.array([[2,],[4,],[7,],[0,]]) # 4*1的列向量bbb
print('\n')
print(bbb)
print('\n')
print(a3 + bbb)

a = np.arange(0,60,5) 
a = a.reshape(3,4)  
b = a.T
print ('原始数组是：') 
print (a) 
print ('\n') 
copy1 = a.copy(order = 'F') # F按列 C按行
print(copy1)
print('\n')
for item in np.nditer(copy1):
    print(item, end = ', ')
    pass
print('\n')

print(b)
for item in np.nditer(b.copy(order="F")):
    print(item,end = ', ')
    pass

# nditer中的可选参数 op_flags 规定只读read-only 或 可读写 read-write 或者 write-only
print('\n','更新前的a')
print(a)
for x in np.nditer(a,op_flags = ['readwrite']):
    x[...] = 2*x # 为什么要在元素x后面加上[...],发现不加的话，不能达到乘二倍的效果
    # x[...] 是修改原 numpy 元素，x 只是个拷贝
    pass
print('更新后的a')
print(a)

# flags = ['external_loop']，当数组的 order 与在循环中指定的 order 顺序不同时， 打印为多个一维数组，
#当相同时，是整个一个一维数组
for x in np.nditer(a, flags = ['external_loop'], order = 'F'): 
    print (x, end=", " ) # [ 0 40 80], [10 50 90], [ 20  60 100], [ 30  70 110],
    pass
print('\n')
for x in np.nditer(a, flags = ['external_loop'], order = 'C'): 
    print (x, end=", " ) # [  0  10  20  30  40  50  60  70  80  90 100 110],
    pass


org = np.arange(9).reshape(3,3)
print('原始数组：')
for row in org:
    print(row)
    pass

# numpy.ndarray.flat 是一个数组元素迭代器
# 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器
print('迭代后的数组：')
for element in org.flat:
    print(element, end = ', ')
    pass

# numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
print('\n')
print(org.flatten()) # 默认按行C的顺序展开
print('F的顺序：')
print(org.flatten(order = 'F'))                           

# numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图
# （view，有点类似 C/C++引用reference的意味），修改会影响原始数组
print ('调用 ravel 函数之后：')
print (org.ravel())
print ('\n')
print ('以 F 风格顺序调用 ravel 函数之后：')
print(org.ravel(order = 'F'))
new1 = org.ravel()
new1[0] = 88 # 尝试修改ravel数组的值
print(new1) # [88  1  2  3  4  5  6  7  8]
print('看看变了没') #发现原始org数组的第一个元素也变成了88
print(org)

# 创建了三维的 ndarray
a3a = np.arange(8).reshape(2,2,2)
 
print ('原数组：')
print (a3a)
print ('获取数组中一个值：')
print(np.where(a3a==0))   
print(np.where(a3a==1))   
print(np.where(a3a==2))   
print(np.where(a3a==3))   
print(np.where(a3a==4))   
print(np.where(a3a==5))
print(np.where(a3a==6))   
print(np.where(a3a==7))   

print(a3a[1,1,0])  # 为 6
print ('\n')

# 将轴 2 滚动到轴 0（宽度到深度）
print ('调用 rollaxis 函数：')
b = np.rollaxis(a3a,2,0)
print (b)
# 查看元素 a3a[1,1,0]，即 6 的坐标，变成 [0, 1, 1]
# 最后一个 0 移动到最前面
print(np.where(b==6))   
print ('\n')




