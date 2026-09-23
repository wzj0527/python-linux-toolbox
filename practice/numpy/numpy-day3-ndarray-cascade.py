# numpy 练习 day3：ndarray 的级联
# axis = 1表示纵轴 axis = 0表示横轴
import numpy as np
"""级联"""
a1 = np.random.randint(0,10,(3,4))
print(a1)
a2 = np.random.randint(10,20,(3,4))
print(a2)
# a3 = np.concatenate((a1,a2),axis=0)# 挨着x轴去级联
# print(a3)
# a4 = np.concatenate((a1,a2),axis=1)# 挨着y轴去级联
# print(a4)
# 注意级联长度一致

# a5 = np.hstack((a1,a2))# 横向级联
# print(a5)
# a6 = np.vstack((a1,a2))# 纵向级联
# print(a6)