# 练习 day6：推导式
# 即生成一个列表
# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list1 = list(range(1, 11))
# print(list1)

# 生成[1x1, 2x2, 3x3, ..., 10x10]
# 1. for循环
# L = []
# for x in range(1,11):
#     L.append(x*x)
# print(L)

# 2. 推导式
# list1 = [x * x for x in range(1,11)]
# print(list1)

# 还可以加入if
# list1 = [x * x for x in range(1,11) if x % 2 == 0]
# print(list1)

# 多层循环,嵌套
# list1 = [m+n for m in 'ABC' for n in 'XYZ']
# print(list1)

# 还可作用于字典d.items()的输出是把字典中的键值对全部取出（返回的是一个视图对象，不会创建生成一个列表）
# 1. for
# d = {'x':'A','y':'B','z':'C'}
# for k,v in d.items():
#     print(k,'=',v)
# 2.推导式
# d = {'x':'A','y':'B','z':'C'}
# print(d.items())
# list1 = [k+'='+v for k,v in d.items()]
# print(list1)

# 还可以用函数
# L = ['Hello', 'World', 'IBM', 'Apple']
# list1 = [s.lower() for s in L]# s是遍历得到的字符串
# print(list1)

# 推导式的if...else
# for 后跟if的话不能跟else因为for后的if只是一个过滤条件
# for 前跟if必须要跟else因为for前是一个表达式

# list1 = [x for x in range(1, 11) if x % 2 == 0]# 过滤式最后会丢弃一部分元素
# print(list1)

# list1 = [x for x in range(1, 11) if x % 2 == 0 else pass]# 会报错
# print(list1)

# list1 = [x if x % 2 == 0 else None for x in range(0, 11)]# 表达式元素不会丢失与一开始的数量相同
# print(list1)

"""练习"""
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
# L = ['Hello', 'World', 18, 'Apple', None]
# list1 = [s.lower() for s in L]# 会报错

# 使用内建的isinstance函数可以判断一个变量是不是字符串：
# x = 'abc'
# y = 123
# print(isinstance(x, str))
# print(isinstance(y, str))

"""请修改列表生成式，通过添加if语句保证列表生成式能正确地执行："""
L = ['Hello', 'World', 18, 'Apple', None]
list1 = [s.lower() for s in L if isinstance(s, str)]
print(list1)
# 测试
if list1 == ['hello','world','apple']:
    print("测试通过")
else:
    print('测试失败')