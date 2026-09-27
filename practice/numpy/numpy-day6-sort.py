# numpy 练习 day6：numpy查找和排序
import numpy as np

# 查找索引np.argmax(),np.argmin() 找最大值和最小值的索引,有相同值得时候只会返回第一个最值得索引
# data = np.random.randint(0,10,5)
# print(data)
# print(np.argmax(data))
# print(np.argmin(data))
# print(data.argmax())

# data = np.random.randint(0,10,(3,3))
# print(data)
# print(data.argmax(axis=0))# 每一列的最值（行方向）
# print(data.argmax(axis=1))# 每一行的最值（列方向）

# 条件查找 np.where(condition,[x,y]) 函数返回输入数组中满足给定条件的元素索引,x,y的意思是条件为真替换为x，条件为假替换y
# data = np.array([1,2,3,4,5])
# condition = data > 2
# print(np.where(condition))
# print(np.where(condition,1,0))# 所以不只能单单输出索引，还能替换去进行些操作,这个操作只是给你返回一个替换后的结果，不会影响原本的数组


# 快速排序
# np.sort()不改变输入
# ndarray.sort()本地处理，不占用空间，但改变输入
# arr = np.random.randint(0,10,5)
# print(arr)
# print(np.sort(arr))
# print(arr)
#
# arr1 = np.random.randint(0,10,5)
# print(arr1)
# print(arr1.sort())
# print(arr1)# 原数组会改变


# 索引排序 np.argsort()函数返回的是数组值从小到大的索引值
# data = np.random.randint(0,10,5)
# print(data)
# print(np.argsort(data))

# arr = np.random.randint(0,10,(3,3))
# print(arr)
# print(np.argsort(arr,axis=0))# 排序列（行方向排序）
# print(np.argsort(arr,axis=1))# 排序行（列方向排序）


# 部分排序
# np.partition(a,k) 有的时候我们不是对全部数据感兴趣，我们可能只对最小或最大的一部分感兴趣,a是数组
# 当k为正时，表示从左往右数，索引 2 的位置是分水岭。左边有 2 个数（索引 0, 1），它们是最小的 2 个数,也一定会挑出第k+1小的数
# 当k为负时，表示从右往左数，倒数第 2 个位置（即索引 n-2）是分水岭。右边有 1 个数（索引 n-1），它是最大的 1 个数。
# data = np.random.permutation(10000)
# print(np.partition(data, -2))
# data = np.random.randint(0,10,5)
# print(data)
# print(np.partition(data,-2))