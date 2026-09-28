# 练习 day8：上下文管理器
# 一个上下文管理器是一个对象，定义了运行时的上下文

# with context as name:  with 后面通常是一个函数调用或者一个对象
# 通常情况下，对于一个文件的写入
# f = open("mytext.txt","w")
# f.write("hello world")
# f.close()

# with open("mytext.text","w") as f:# 不需要关闭文件，因为with操作结束后会自动关闭文件
#     f.write("hello world")

# 算一个时间试试
import time
# start = time.perf_counter()# cpu运行这行的时间
# nums = []
# for n in range(10000):
#     nums.append(n ** 2)
# stop = time.perf_counter()
# elapsed = stop - start
# print(elapsed)

# 变一下程序，通过上下文管理器
# class Timer:# 类里面有enter和exit就称它为上下文管理器的类
#     def __init__(self):
#         self.elapsed = 0
#         # self 接收的是创建对象传入的实例对象，它和后面 __enter__ 返回的 self 是同一个对象
#     def __enter__(self):
#         self.start = time.perf_counter()
#         return self# 返回当前with创建的Timer的实例对象，这个实例对象里的所有方法和属性都能使用
#         # 返回当前实例对象。这个返回值会被赋给 with 语句中 as 后面的变量（timer）
#     def __exit__(self, type, value, traceback):
#         self.end = time.perf_counter()
#         self.elapsed = self.end - self.start
#
# with Timer() as timer:# with会在开头调用对象的enter方法，在with中内容结束会自动调用对象的exit方法
#     # timer 接收的是 __enter__ 的返回值（也就是当前 Timer 实例）
#     nums = []
#     for n in range(10000):
#         nums.append(n ** 2)
# print(timer.elapsed)# with 不会创建新作用域，所以外面依然可以访问 timer 实例


# 装饰器写法
from contextlib import contextmanager
import time
@contextmanager
def Timer():
    start = time.perf_counter()
    yield# 之前在enter中发挥作用，之后再exit发挥作用,yield返回None
    end = time.perf_counter()
    print(end - start)

with Timer():
    nums = []
    for n in range(10000):
        nums.append(n ** 2)

# with Timer() 时，__enter__ 唤醒生成器，跑到 yield 暂停，返回 yield 的值。然后 with 块内部的代码运行。
#等 with 块结束，__exit__ 再次唤醒同一个生成器，从 yield 后面继续跑，记录结束时间并打印。
