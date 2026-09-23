# numpy 练习 day2：数组生成函数（ones/zeros/full/eye/linspace/arange/random 系列）
import numpy as np
# 1.np.ones(shape,dtype=None ,order='C') 用1构造指定形状的高维数组
# ar1 = np.ones(shape = (2,3),dtype = np.int8 )# 注意（1，3）和（3，）
# print(ar1)

# 2. np.zeros(shape,dtype = float ,order = 'C') 用0区构造指定形状
# ar1 = np.zeros(shape=(3,3),dtype=np.uint8)
# print(ar1)

# 3. np.full(shape,fill_value,dtype = None, order='C') 与上面相同但是fill_value可以指定数据
# ar1 = np.full(shape = (3,3),fill_value = 6, dtype = np.int8)
# print(ar1)

# 4. np.eye(N,M = None ,k = 0,dtype=float) 生成一个单位矩阵,N是维数，M能控制列数，k控制对角线偏移（左加右减）
# ar1 = np.eye(N = 3 , k = 1)
# print(ar1)

# 5. np.linspace(start,stop,num = 50,endpoint = True,retstep = False,dtype = None)
# 生成等差数列，start 起始，stop 终值，num 个数,endpoint就是要不要终点值
#
# ar1 = np.linspace(0,100,10,endpoint=False)
# print(ar1)
# ar1 = np.linspace(0,360,4,endpoint=False)
# print(ar1)# 360°取0，90，180，270控制endpoint

# 6. np.arange(start,stop,step,dtype=None)
# ar1 = np.arange(0,100,step = 10)
# print(ar1) # 5,6比较相似


# 7. np.random.randint(low,high=None,size=None,dtype)# 构造随机数组,只能生成整数
# ar1 = np.random.randint(0,100,(3,5))
# print(ar1)


# 8. 正态分布函数
# np.random.randn(维度)标准正态
# np.random.normal(loc,scale,size)普通正态loc是数学期望值，scale是数学方差

# ar1 = np.random.normal(175,10,(3,3))
# print(ar1)

# ar1 = np.random.randn(3,3)
# print(ar1)


# 9. np.random.random(size) 生成0-1的随机数,只会出现0不会出现1
# ar1 = np.random.random((3,3))
# print(ar1)


# 10. np.random.permutation(数量)生成随机索引，索引的意思就是数据一定从0开始，不能是1-num
# ar1 = np.random.permutation(10)
# print(ar1)

# 11. 随机种子
# np.random.seed(0)# 添加一个种子，就会限制下面，固定随机出来的数组，种子不变数组不变
# ar1 = np.random.randint(0,10,(5,))
# print(ar1)
