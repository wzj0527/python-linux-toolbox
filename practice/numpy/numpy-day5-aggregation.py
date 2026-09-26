# numpy 练习 day5：ndarray 的聚合操作
import numpy as np
# 求和np.sum，整个数组求和
# data = np.random.randint(0,100,5)
# print(data)
# print(data.sum())
# data = np.random.randint(0,100,(3,4))
# print(data)
# print(data.sum())
# print(data.sum(axis=0))# 求每一列（行方向）的和
# print(data.sum(axis=1))# 求每一行（列方向）的和

# numpy表示空值
# print(np.nan)
# print(type(np.nan))

# nan与任何数值计算都为空,无论加减乘除
# data = np.random.randint(0,10,10)
# data = data.astype(np.float32)
# print(data)
# data[1] = np.nan
# print(data)
# print(data.sum())# 输出为nan
# print(np.nansum(data))# 去掉nan之和


# 最大值最小值
# arr = np.random.randint(0,10,(3,4))
# print(arr)
# print(arr.max())
# print(arr.min())
# np.mean求均值 np.prod求累积 np.std求标准差 np.var求方差 np.median求中位数 np.percentile求分位数

# any(是不是至少有一个True) 和 all（全都是True） 检查bool类型数组
# ar1 = np.random.randint(0,2,10).astype(np.bool)
# print(ar1)
# print(ar1.any())
# print(ar1.all())

"""练习"""
"""生成一个Python成绩列表，假设有100人，满分100分，及格60分，如何计算班级的及格率"""
# ar1 = np.random.randint(0,100,100)
# print(ar1)
# pass_lv = ((ar1 > 59).astype(int)).mean()
# pass_lv1 = ((ar1 > 59)*1).mean()
# print(pass_lv)
# print(pass_lv1)

"""标准化就是将一组输数据进行如下规则的转换：减去期望值再除以标准方差，请封装一个函数来实现"""
# def std(data):
#     return (data-np.mean(data))/np.std(data)
#
# ar1 = np.random.randint(1,100,100)
# print(std(ar1))

"""随机生成一个一维数组，比较其中是否有至少一个数据大于3倍平均值"""
# ar1 = np.random.randint(0,50,5)
# print(ar1)
# result = ar1 > 3*np.mean(ar1)
# print(result.any())

"""生成1000行3列的一个标准正态分布数组，查询每一列是否存在至少一个数据大于该列的3倍标准差"""
# ar1 = np.random.randn(1000,3)
# std1 = ar1.std(axis=0)*3
# print(std1)
# print(np.any(ar1>std1,axis=0))

"""如何检查两个形状相同的数组数值是完全一致的"""
ar1 = np.random.randint(1, 10, (3,3))
ar2 = np.random.randint(1, 10, (3,3))
print(np.all(ar1 == ar2))
ar3 = np.ones((3,3))
ar4 = np.ones((3,3))
print(np.all(ar4 == ar3))