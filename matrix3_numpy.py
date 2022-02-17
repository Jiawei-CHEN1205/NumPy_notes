
import numpy as np
 
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])  
 
# 对 y 广播 x
b = np.broadcast(x,y)  
# 它拥有 iterator 属性，基于自身组件的迭代器元组
print(x)
print(y)
print(b)
print ('对 y 广播 x：')
r,c = b.iters
 
# Python3.x 为 next(context) ，Python2.x 为 context.next()
print (next(r), next(c))
print (next(r), next(c))
print (next(r), next(c))
print (next(r), next(c))
print (next(r), next(c))
print (next(r), next(c))
print (next(r), next(c))
print (next(r), next(c))
print (next(r), next(c))

print ('\n')
# shape 属性返回广播对象的形状
 
print ('广播对象的形状：')
print (b.shape)
print ('\n')
# 手动使用 broadcast 将 x 与 y 相加
b = np.broadcast(x,y)
c = np.empty(b.shape) #空的数组
 
print ('手动使用 broadcast 将 x 与 y 相加：')
print (c.shape)
print ('\n')
c.flat = [u + v for (u,v) in b]
 
print ('调用 flat 函数：')
print (c)
print ('\n')
# 获得了和 NumPy 内建的广播支持相同的结果
 
print ('x 与 y 的和：')
print (x + y)



a = np.arange(16).reshape(4, 4)
print('第一个数组：')
print(a)
print('\n')

print('沿水平方向分割：')
d= np.hsplit(a,2)
print(d)

print('默认分割（0轴）：')
b = np.split(a,2)
print(b)
print('\n')