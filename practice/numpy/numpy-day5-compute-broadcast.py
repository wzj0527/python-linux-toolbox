# numpy 练习 day5：ndarray 的基本运算和广播机制
"""基本运算原则"""
# 加法
import numpy as np
# arr = np.random.random(10)
# print(arr)
# arr2 = np.random.randint(0,10,10)
# print(arr2)
# arr3 = arr + arr2
# print(arr3)# 对应相加，与矩阵相同


# 大小比较
# arr = np.random.randint(0,10,(3,4))
# print(arr>5)# 数组里的每个数作比较

# 乘法
# arr1 = np.random.randint(0,10,(3,4))
# print(arr1)
# arr2 = np.random.randint(0,10,(3,4))
# print(arr2)
# print(arr1 * arr2)# 与矩阵不同，这个是对应位置相乘

# 除法
# arr1 = np.random.randint(1,10,(3,4))
# print(arr1)
# arr2 = np.random.randint(1,10,(3,4))
# print(arr2)
# print(arr1 / arr2)# 注意分母不能为0，同样也是对应元素相除

"""广播机制"""
# 两个数组的后缘维度的轴长度相符或其中的一方的长度为1，则认为它们是广播兼容的。
# 广播会在缺失和长度为1的维度上进行
# 后缘维度指的是从末尾算起的维度（3，2）与（4，3，2）轴长度指的是后缘维度大小是否相同比如2和2，3和3
"""例子"""
# 1
# a = np.ones((2,3))
# b = np.arange(3)
# print(a)
# print(b)
# print(a+b)

# 2
# a = np.ones((4,3,2))
# b = np.random.randint(0,10,(3,2))
# print(a)
# print(b)
# print(a+b)

# 3
# a = np.arange(3).reshape((3,1))
# b = np.arange(3)
# print(a)
# print(b)
# print(a+b)

# 4
# a = np.arange(3)# 0维可以跟任何数组广播相加
# print(a)
# print(a+1)

"""习题"""
"""a = np.ones((4,1)),b = np.arange(4),求a + b"""
# a = np.ones((4,1))
# b = np.arange(4)
# print(a)
# print(b)
# print(a+b)
"""假设有100个员工考勤需要处理，由于上个月统一调休，所以需要将所有人的总考勤天数-1，如何操作"""
# ar = np.random.randint(0,22,(10,10))
# print(ar)
# new_ar = ar-1
# print(new_ar)

"""假设员工上班时间表通过np.random.randint(7,10,100)获取，如何快速找到上班时间不足8小时的员工"""
ar = np.random.randint(7,10,100)
print(ar < 8)