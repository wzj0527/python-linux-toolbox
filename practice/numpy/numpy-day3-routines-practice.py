# numpy 练习 day3：routines 综合练习（随机数组/等差数列/0-1随机/圆等分弧度）
import numpy as np
# """创建一组形状为（3，4）的二维数组，取值范围为（-5，5）"""
# ar1 = np.random.randint(-5,5,(3,4))
# print(ar1)
# """创建一组等差数列，步长为3，数组长度为5"""
# ar2 = np.arange(0,15,3)
# print(ar2)
# """构造一个3维取值范围为0-1的随机数组，数据类型为np.float64,形状为（100，100，3）"""
# ar3 = np.random.random((100,100,3))
# print(ar3.dtype)
# print(ar3)
# """已知pi在numpy中是一个预制的常量，可以使用np.pi访问。计算出将一个圆等分成8份的弧度的代码"""
ar4 = np.arange(0,2*np.pi,np.pi/4)
print(ar4)
