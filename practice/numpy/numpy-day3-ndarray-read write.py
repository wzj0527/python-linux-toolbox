# numpy 练习 day3：ndarray 的读写操作

import numpy as np
"""索引访问"""
# arr4 = np.random.randint(0,10,10)
# print(arr4)
# print(arr4[0])
#
# arr4 = np.random.randint(0,10,(3,4))
# print(arr4)
# print(arr4[2][0])# 这个叫间接访问，不推荐
# arr4[2][0] = 100
# print(arr4)
# # 也可以这样访问
# print(arr4[2,0])# ndarray特有的方式

"""列表访问"""
# arr1 = np.random.randint(0,100,10)
# index1 = [1,2]# 去某些索引的值
# print(arr1[index1])
# index2 = np.random.permutation(10)
# print(arr1[index2])# 对原数组进行随机排序

# 在原始数据中随机取出三个数
# random_index = np.random.permutation(10)[[0,1,2]]
# print(arr1[random_index])

# 高维数组中使用
# arr2 = np.random.randint(0,100,(5,5))
# # print(arr2[[0,1]])
# print(arr2[:,[0,1]])# 取了5行,然后取5行中的前两列

"""切片访问"""
# arr1 = np.random.randint(0,100,10)
# print(arr1)
# print(arr1[0:3])
# print(arr1[-4:])
# print(arr1[1::2])

"""bool列表访问"""
# arr3 = np.random.randint(0,100,5)
# print(arr3)
# bool_index = [False, True, True, False, True]
# print(arr3[bool_index])


"""练习"""
"""构建一个长度为10的随机数组，进行逆序输出"""
# arr1 = np.random.randint(0, 100, 10)
# print(arr1)
# print(arr1[::-1])

"""构造一个形状为（5，4）的二维数组，提取最后两列，使用3种方法"""
# arr2 = np.random.randint(0, 100, (5,4))
# print(arr2)
# # 1
# print(arr2[:,[2,3]])
# 2
# index_bool = [False, False, True, True]# 这个是二维的，注意坑
# print(arr2[:,index_bool])
# 3 切片
# print(arr2[:,2:4])


"""构建一个6行5列的数组，对数组进行行方向的随机排序"""
# arr3 = np.random.randint(0, 100, (6,5))
# print(arr3)
# index1 = np.random.permutation(6)
# print(index1)
# print(arr3[index1])