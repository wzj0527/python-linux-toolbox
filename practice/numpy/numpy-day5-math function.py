# numpy 练习 day5：ndarray 的数学函数

import numpy as np
# 三角函数sin，cos，tan
# arr = np.random.random(10)
# print(arr)
# 将上述变到-pi到pi之间
# arr1 = arr*2*np.pi - np.pi
# print(arr1)
# print(np.sin(arr1))

# numpy里面接受的是弧度,不是角度，下面为例
# print(np.sin(np.pi/2),np.sin(90))

# 舍入函数,np.around(a,decimals)
# a数组
# decimals:舍入的小数位数，默认为0，如果为负，整数将四舍五入到小数点左侧的位置
# data = np.random.random(10)
# print(data)
# print(np.around(data,3))
# print(np.around([1.1,2.6,5.6],-1))# 输出为[0,0,10]相当于看十位，用个位决定四舍五入

# 算数函数，加减乘除add,subtract,multiply,divide
# np.power幂运算，np.mod求余运算
# np.log自然底数对数运算，np.log2(),np.log10()
# a1 = np.random.randint(0,10,(4,3))# 支持广播
# a2 = np.random.randint(0,10,3)
# print(a1)
# print(a2)
# print(np.add(a1,a2))
# print(a1+a2)

# 幂运算
# print(np.power(2,3))# 输出为8
# data = np.random.randint(0,10,5)
# print(data)
# print(np.power(data,2))# 每个元素进行平方
# print(np.power(data,1/2))# 每个元素开方

# 求余运算
# print(np.mod(5,2))# 求余为1
# data = np.random.randint(0,20,5)
# print(data)
# print(np.mod(data,3))

# 对数
print(np.log(np.e))# 输出为1
data = np.random.randint(0,10,5)
print(data)
print(np.log2(data))