# 练习 day10：GIL 和 asyncio
# CPU 密集任务（大量计算）→ 多线程没用，甚至更慢（因为 GIL 锁切换有开销）
# I/O 密集任务（网络请求、文件读写、等待）→ 多线程有用（等待时 GIL 会释放）
# 进程比线程更大一点，一个进程可以有多个线程
# 进程不止有一个线程的时候就会发生竞争冒险，可能会导致内存泄漏
# 防止上述情况，就会加锁，使得一个线程运行时别的线程不能访问
# 但是由于内容多，GIL就出现了，是全局锁
# GIL使得python的多线程无法利用多核，因为会锁,别的无法访问


# asyncio
# 1.协程 计算机不提供，人为创造的，让代码在一个线程中能来回切换运行代码

# 1 greenlet实现
# from greenlet import greenlet
#
# def fun1():
#     print(1)
#     gr2.switch()
#     print(2)
#     gr2.switch()
#
# def fun2():
#     print(3)
#     gr1.switch()# 切换的时候有中断
#     print(4)
#
#
# gr1 = greenlet(fun1)
# gr2 = greenlet(fun2)
# gr1.switch()# 切换的意思


# 2 yield
# def fun1():
#     yield 1
#     yield from fun2()
#     yield 2
#
# def fun2():
#     yield 3
#     yield 4
#
# f1 = fun1()
# for item in f1:
#     print(item)

# 3 asyncio
# import asyncio
# async def fun1():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#
# async def fun2():
#     print(3)
#     await asyncio.sleep(2)
#     print(4)
#
# async def main():
#     tasks = [
#         asyncio.create_task(fun1()),
#         asyncio.create_task(fun2())
#         ]
#     await asyncio.wait(tasks)# 等 fun1 和 fun2 都跑完
#
# asyncio.run(main())


# 学习
# async def func():
#     pass
# result = func()# 这里函数内部代码不会执行，result得到的一个协程对象

# 简单用法
# import asyncio
# async def func():
#     print("123")
#     response = await func2()
#     print("678",response)
#
# async def func2():
#     print("456")
#     return 'func2结束'
#
# result1 = func()
# asyncio.run(result1)

# Task对象,帮助在事件循环中添加多个任务
# import asyncio
#
# async def func():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return "返回值"
#
# async def main():
#     print("main开始")
#     # 创建Task对象，将当前执行func函数任务添加到事件循环
#     tasks = [
#         asyncio.create_task(func(),name = "n1"),
#         asyncio.create_task(func(),name = "n2")
#     ]
#
#     print("main结束")
#     done,pending = await asyncio.wait(tasks)# 等任务全部完成，返回done和pending，任务完成所有的返回值会放在done中
#     # pending是没有完成的任务，tasks后面可以跟timeout = n s最多等待n秒
#     print(done)
# asyncio.run(main())



# gather 更简洁的写法，但是无法设超时
# import asyncio
#
# async def hello(name):
#     print(f"{name} 开始")
#     await asyncio.sleep(1)
#     print(f"{name} 结束")
#
# async def main():
#     results = await asyncio.gather(hello("A"), hello("B"), hello("C"))
#     print(results)
# asyncio.run(main())
