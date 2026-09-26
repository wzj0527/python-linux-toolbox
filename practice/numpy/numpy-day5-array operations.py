# numpy 练习 day5：ndarray 的数组操作
import numpy as np
# 添加元素 np.append(arr,values,axis)
# arr = np.array([1,2,3,4])
# print(arr)
# new_arr = np.append(arr,5)
# print(new_arr)
# arr = np.random.randint(0,10,(4,3))
# print(arr)
# new_arr = np.append(arr,[[1,2,3]],axis=0)# 需要相同的维度，相同的长度，如果维度不同，数组可能会被扁平处理或者报错
# print(new_arr)


# 插入元素，在给定索引之前，沿给定轴在输入数组中插入值
# 如果未提供轴，则输入数组会被展开np.insert(arr,位置,values,axis)
# arr = np.array([1,2,3,4,5])
# print(arr)
# new_arr = np.insert(arr,2,100)
# print(new_arr)
# arr = np.random.randint(0,10,(4,3))
# print(arr)
# new_arr = np.insert(arr,2,[1,1,1,1],axis = 1)# 插入要低一维元素
# print(new_arr)


# 删除元素。函数返回从输入数组中删除指定子数组的数组
# 如果未提供轴参数，则输入数组将展开
# arr = np.array([1,2,3,4,5])
# print(arr)
# new_arr = np.delete(arr, 2)
# print(new_arr)
# arr = np.random.randint(0,10,(4,3))
# print(arr)
# new_arr = np.delete(arr,1,axis=1)
# print(new_arr)


# 数组的变形reshape
# np.reshape(arr,newshape,order='C')
# newshape新的形状应当兼容原有形状,数量上要保持一致
# order：'C'--按行 'F'--按列，'A'--原顺序 'k'--元素在内存中出现顺序，重新排序的顺序，后两个几乎不用
# arr = np.random.randint(0,10,8)
# print(arr)
# new_arr = np.reshape(arr,(2,4))# 不能写shape=（2，4），numpy中，有些函数的参数名可以写，有些函数的参数名不能写
# print(new_arr)


# arr = np.random.randint(0,10,8)
# print(arr)
# new_arr = np.reshape(arr,(2,4))
# print(new_arr)
# new_arr1 = np.reshape(arr,(2,4),'F')
# print(new_arr1)


# 数组迭代器，numpy.ndarray.flat
# 高纬的for循环迭代会一行一行的输出
# arr = np.random.randint(0,10,(4,3))
# print(arr)
# for i in arr.flat:
#     print(i)

# 数组的扁平处理
# arr = np.random.randint(0,10,(4,3))
# print(arr)
# print(arr.flatten())# 返回一份展开的数组拷贝，对拷贝所做的修改不会影响原始数组
# print(np.ndarray.flatten(arr))
# print(arr.ravel())# 返回一个展开的数组引用，修改会影响原始数组
# print(np.ndarray.ravel(arr))
# 区别就是是否能独立操作，是否创建了一块新的内存放副本
# 例子如下,arr与ravel是同一个东西进行的操作，而flatten另一个内存的副本
# arr_view = arr.ravel()
# print(arr_view)
# arr_view[0] = 99
# print(arr)
#
# arr_copy = arr.flatten()
# print(arr_copy)
# arr_copy[0] = 1
# print(arr)


# 数组翻转 np.transpose，对于维度上的调换,转置
arr = np.random.randint(0,10,(4,3))
print(arr)
# new_arr = np.transpose(arr)
# print(new_arr)

# 或者对某些轴进行操作
new_arr = arr.transpose([1,0])# 新数组的0轴放原来的1轴，新数组的1轴放原来的0轴
print(new_arr)
