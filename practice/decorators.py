# 练习 day9：带参装饰器
# def outer(func):
#     def inner(*args, **kwargs):
#         print("准备开始")
#         func(*args, **kwargs)
#         print("执行结束")
#     return inner
#
# @outer # send_wechat = outer(send_wechat)
# outer(send_wechat)返回的是inner函数，所以新的send_wechat其实就是inner函数
# 而inner中的func是之前传入的send_wechat函数
# def send_wechat(body):
#     print("微信",body)
#
# def send_email():
#     print("邮件")
#
# def send_sms():
#     print("短信")
# send_wechat("你好")
# 含参时候原本send_wechat传入func（）此时需要一个形参，因为此时是等于旧的send_wechat含有参数
# 而新的send_wechat在最后使用的时候调用，他等同于x（）故也需要参数
from pydoc import text

# 装饰器返回值
# def outer(func):
#     def inner(*args, **kwargs):
#         value =  func(*args, **kwargs)
#         return value
#     return inner
#
# @outer
# def send_wechat(body):
#     print("微信")
#     return body
#
# res = send_wechat("你好")
# print(send_wechat.__name__)# 函数名是inner
# print(res)

# 更复杂的带参装饰器
# def log(text1):# text1这个参数说白了就是服务inner的，
#     # 比如两个不同的函数需要同一种功能装饰器的不同参数运行的功能，
#     # 这样就可以通过log传入修改那个参数省的同一功能写两次
#     def outer(func):
#         def inner(*args, **kwargs):
#             res = func(*args, **kwargs)
#             print(text1)
#             return res
#         return inner
#     return outer
# @log('test')  # send_wechat = log('text')(send_wechat)
# # 首先执行log('text')，返回的是outer函数，
# # 再调用返回的函数，参数是send_wechat函数，返回值最终是inner函数。
# def send_wechat(data):
#     print('微信', data)
#
# send_wechat('你好')
#
# print(send_wechat.__name__)

# 考虑到最后装饰后的函数输出对象为inner
# 所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
# 并且报错时显示的是 send_wechat 而不是 inner，好定位
# import functools
# def log(text1):
#     def outer(func):
#         @functools.wraps(func)# 不需要编写inner.__name__ = func.__name__这样的代码，
#         # Python内置的functools.wraps就是干这个事的
#         def inner(*args, **kwargs):
#             res = func(*args, **kwargs)
#             print(text1)
#             return res
#         return inner
#     return outer
# @log('test')
# def send_wechat(data):
#     print('微信', data)
#
# send_wechat('你好')

# print(send_wechat.__name__)# 输出为send_wechat



"""练习"""
import functools,time


# def outer(func):
#     @functools.wraps(func)
#     def inner(*args, **kwargs):
#         start = time.perf_counter()
#         value = func(*args, **kwargs)
#         end = time.perf_counter()
#         elapsed = end - start
#         print('%s executed in %s ms' % (func.__name__, elapsed))
#         return value
#     return inner
#
# @outer
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
#
# @outer
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
# else:
#     print("测试成功")

# 2.
from functools import wraps

def retry(max_attempts = 3 , delay = 1):
    def decorator(func):
        @wraps(func)                    # 保留原函数 __name__
        def wrapper(*args, **kwargs):   # *args/**kwargs 兼容任意函数
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)# 如果失败，这里不会有返回值，并且会被抛出异常，下一句异常被捕获
                except Exception as e:
                    print(f"第{i+1}次失败: {e}")
                    time.sleep(delay)
            raise RuntimeError("重试耗尽")
        return wrapper
    return decorator

import random
@retry(max_attempts=3, delay=0.5)
def risky():
    if random.random() < 0.7:
    # risky 里 random.random() < 0.7，如果踩中 70% 概率,输出raise ValueError("运气不好")
    # 这个异常被 except Exception 捕获打印"第1次失败" → 睡 0.5 秒
        raise ValueError("运气不好")
    return "成功"

print(risky())