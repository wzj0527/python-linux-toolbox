# numpy 练习 day4：ndarray 的切分操作
import numpy as np

# arr = np.random.randint(0,100,(6,5))
# print(arr)
# ar1,ar2 = np.split(arr,indices_or_sections=2,axis=0)# indices_or_sections可以传入整数或者一维的数组 整数就是分为N等分,要求必须能被N整除
# print(ar1)
# print(ar2)

# indices_or_sections[m,n]表达的是按照 0:m,m:n,n:的切片逻辑进行对数组拆分（左闭右开区间）
# ar3 = np.split(arr,indices_or_sections=[2],axis=1)
# print(ar3)
# ar4 = np.split(arr,indices_or_sections=[2,3],axis=1)
# print(ar4)
# ar5 = np.split(arr,indices_or_sections=[2,3,4],axis=1)
# print(ar5)

# ar1  = np.vsplit(arr,2) # 纵轴横着砍一刀(纵轴切)
# print(ar1)
# ar1 = np.hsplit(arr,[2,3])# 横轴切
# print(ar1)
"""级联和切分练习"""
"""生成两个形状分别为(4,4)和(8,4)的二维整型数组,尝试级联"""
# ar1 = np.random.randint(10,20,(4,4))
# print(ar1)
# ar2 = np.random.randint(10,20,(8,4))
# print(ar2)
# ar3 = np.concatenate((ar1,ar2),axis=0)
# print(ar3)
"""使用两种方法,将上题级联的结果保存并拆分成三等分"""
# ar4 = np.split(ar3,3,axis=0)
# print(f"拆分后的{ar4}")
#
# ar5 = np.vsplit(ar3,3)
# print(ar5)

"""生成一个长度为5的一维整型数组,将类型修改为float32"""
ar6 = np.random.randint(0,10,5)
print(ar6.dtype)
ar7 = ar6.astype(np.float32)
print(ar7.dtype)
print(ar7)