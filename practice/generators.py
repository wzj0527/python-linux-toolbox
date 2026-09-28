# 练习 day7：生成器
# 创建一个generators
# 1.将推导式[]换成()，就变成了生成器
# from turtle import done
#
# g = (x * x for x in range(10))
# print(g)
# print(next(g))
# print(next(g))# 将生成器的内容挨个输出
# print(next(g))
# print(next(g))


# 显然可以for迭代去输出g
# for i in g:
#     print(i)

# 斐波拉契数列
# def fib(max):
#     n,a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a,b = b,a+b
#         n = n + 1
#     return done
# print(fib(5))
# 将print（b）修改为yield b 就变成generator函数
def fib(max):
    n,a, b = 0, 0, 1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1
    return None
# for n in fib(4):
#     print(n)
# 普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# yield相当于一个函数中断
# 以下为例,不会每次从头开始
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 3
#     print('step 3')
#     yield 5
# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))
# 这里需要注意一个点，关于generator对象，多次调用generator函数会创建多个相互独立的generator。
# print(next(odd()))
# print(next(odd()))
# print(next(odd()))# 上面三个输出一样是因为odd()会创建一个新的generator对象，上述相当于创建了3个完全独立的generator


# generator使用for循环拿不到返回值，想要拿到返回值可以必须捕获StopIteration错误，返回值包含在StopIteration的value中
# 以下为例子
# for 一旦遇到 StopIteration 异常，就自动捕获并结束循环，直接忽略 return 的值
# 而 next() 会返回每一次 yield 的值，最后一次会因为生成器结束而抛出 StopIteration 异常，
# 此时必须用 try...except 捕获这个异常，才能拿到 return 的值（在异常对象的 e.value 里）
for n in fib(6):
    print(n)

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break



"""练习"""
# 杨辉三角
# def triangles(max):
#     list1,n = [1],0
#     while n < max:
#         yield list1
#         list1 = [1] + [list1[i] + list1[i+1] for i in range(len(list1) - 1)] + [1]
#         n += 1
# # 测试
# results = []
# for t in triangles(10):
#     results.append(t)
#
# for t in results:
#     print(t)
#
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')