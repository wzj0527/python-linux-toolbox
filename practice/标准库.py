"""os模块 用于和操作系统进行交互"""
import logging
import os

# 1. os.name # 指示正在使用的工作平台（返回操作系统类型）
# print(os.name) # 输出nt，windows返回nt，linux返回posix

# 2.os.getenv(环境变量名称)  #读取环境变量
# print(os.getenv("path"))

# 3.os.path.split() # 分割路径,把目录名和文件名分离，以元组的形式接收，第一个元素是目录路径，第二个元素是文件名
# print(os.path.split(r"C:\Users\wuzhijian\Desktop\python\标准库.py"))

# 4.os.path.dirname  # 显示split的第一个元素
# print(os.path.dirname(r"C:\Users\wuzhijian\Desktop\python\标准库.py"))
# 5.os.path.basename # 显示split的第二个元素
# print(os.path.basename(r"C:\Users\wuzhijian\Desktop\python\标准库.py"))

# print(os.path.basename(r"C:\Users\wuzhijian\Desktop\python/"))
# 如果路径以/结尾就返回空值，\结尾就报错

# 6.os.path.exists() # 判断路径（文件或目录）是否存在
# print(os.path.exists(r"C:\Users\wuzhijian\Desktop\python/")) # 这个/可以不存在

# 7.os.path.isfile() # 判断文件是否存在
# print(os.path.isfile(r"C:\Users\wuzhijian\Desktop\python\标准库.py"))# 没有文件就是False

# 8.os.path.isdir() # 判断目录是否存在
# print(os.path.isdir(r"C:\Users\wuzhijian\Desktop\python"))# 包含文件名就是False

# 9.os.path.abspath() # 获取当前路径下的绝对路径
# print(os.path.abspath('GIL-asyncio.py'))
# 10.os.path.isabs() # 判断是否为绝对路径，但是不管你有没有文件
# print(os.path.isabs(str(os.path.abspath('5.py'))))

"""更常用的"""
# 1. os.makedirs() 创建目录
# os.makedirs("a/b/c",exist_ok=True) # exist_ok=True 已存在不报错

# 2.os.listdir(".") 列出目录内容
# print(os.listdir("."))

# 3.os.getcwd() 当前工作目录
# print(os.getcwd())

# 4.os.path.join() 拼接目录
# path = os.path.join("a","b","c.txt")
# print(path)

# 5.os.remove("某文件") 删除文件
# os.remove(r"C:\Users\wuzhijian\Desktop\python\a\test.txt")

"""logging模块,用来记录日志信息"""
# 级别排序从高到底CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
import logging
# logging.debug("我是debug")
# logging.info("我是info")
# logging.warning("我是warning")
# logging.error("我是error")
# logging.critical("我是critical")
# logging只会显示大于等于warning的信息

# 1.logging.basicConfig() # 配置root logger
#   1.filename: 指定日志文件的文件名，所有会显示的日志都会存放到这个文件中
# logging.basicConfig(filename='log.log')
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

#   2.filemode:文件的打开方式，默认是a（追加模式）w写会覆盖
# logging.basicConfig(filename='log.txt',filemode='a')
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

#   3.level指定日志显示级别，默认是warning
# logging.basicConfig(filename='log.txt',filemode = 'w',level = logging.NOTSET)
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

#   4.format:指定日志信息的输出格式
logging.basicConfig(filename='log.txt',filemode = 'w',level = logging.NOTSET,format = '%(levelname)s:%(asctime)s \t %(message)s' )
# %(levelno)s 打印日志的级别数值
# %(levelname)s 打印日志级别名称
# %(pathname)s  打印当前执行程序的路径
# %(filename)s  打印当前执行程序名称
# %(funcName)s  打印日志的当前函数
# %(lineno)d   打印日志的当前行号
# %(asctime)s  打印日志的时间
# %(thread)d  打印线程id
# %(threadName)s 打印线程名称
# %(process)d 打印进程id
# %(message)s 打印日志信息
# %(name)s  打印logger的名字
# %(module)s 调用日志输出函数的模块名
# %(created)f LogRecord的创建时间，也就是当前时间，time.time()
# %(msecs)d  LogRecord的创建时间的毫秒部分
# %(relativeCreated)d  输出日志信息的，自logger创建以来的毫秒数
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")




"""json"""
# json.dumps(): 对数据进行编码
# json.loads(): 对数据进行解码。
import json
# data = {
#     'no' :1,
#     'name' : 'Runoob',
#     'url' : 'https://www.runoob.com'
# }
# Python 字典类型转换为 JSON 对象
# json_str = json.dumps(data)
# print("Python 原始数据:", data)
# print("JSON对象", json_str)
# # 将 JSON 对象转换为 Python 字典
# data1 = json.loads(json_str)
# print(data1['name'])

# json.dumps(obj) 转成一个字符串 返回字符串，你自己拿
# json.dump(obj, f)	直接写进文件 返回 None（没返回值）
# # 写入JSON文件
# with open('data.json','w',encoding = 'utf-8') as f:
#     json.dump(data,f)
# # 读取JSON文件数据
# with open('data.json','r',encoding = 'utf-8') as f:
#     data = json.load(f)
# print(data)

# 中文注意点
# data = {"name": "小明"}
# s = json.dumps(data)
# print(s)   # {"name": "\u5c0f\u660e"}  ← 中文变成 \u 转义了，看不懂
#
# s = json.dumps(data, ensure_ascii=False)
# print(s)   # {"name": "小明"}  加上这个参数，中文正常显示

"""collections"""
# counter是一个简单的计数器，例如，统计字符出现的个数，并且会根据出现次数从大到小排列好
# 一般用来统计数据容器的数据
from collections import Counter
# data = Counter("hello world")
# print(data)


# Counter的方法
# 1.elements() 返回一个迭代器，其中每个元素将重复出现计数值所指定次。
# 元素返回的顺序是按照元素在原本序列中首次出现的顺序
# str1 = "hello world"
# res = Counter(str1)
# print(res)
# print(list(res.elements()))

# 2.most_common()返回一个列表，其中包含n个出现次数最高的元素及出现次数，按常见程度由高到低排序
# 如果 n 被省略或为None， 将返回计数器中的所有元素
# str1 = "hello world"
# res = Counter(str1)
# print(res.most_common(2))

# 3.subtract()将两个Counter相减，a.subtract(b)，a中计数减少相应的个数
# a = Counter("hello world")
# print(a)
# b = Counter("hello")
# print(b)
# a.subtract(b)
# print(a)


# defaultdict作用就是在字典查找不存在的key时返回一个默认值而不是KeyError
# 为添加到字典中的每一个key增加一个默认值，当查询一个不存在的元素时，会返回该默认类型和添加一个可写实例变量。
from collections import defaultdict
# value为列表
# dict_demo = defaultdict(list)
# arr = [("yello", 1),("blue", 2), ("green",3), ("yello", 9)]
# for key,value in arr:
#     dict_demo[key].append(value)# defaultdict是自动创建key和value，能指定value的存储形式
# print(dict_demo)

# value为数字
# dict_demo = defaultdict(int)
# count = [("a",1),("b",2),("c",3),("a",4)]
# for key,value in count:
#     dict_demo[key] += value
# print(dict_demo)


# dict_demo = defaultdict(str)  默认值：空字符串
# dict_demo = defaultdict(int)  默认值：0
# dict_demo = defaultdict(list) 默认值：空列表
# dict_demo = defaultdict(dict) 默认值：空字典
# dict_demo = defaultdict(tuple) 默认值：空元素
# dict_demo = defaultdict(set)  默认值：空集合


# deque是为了高效实现插入和删除操作的双向链表结构,双端队列
# 队列：就像排队一样——从一端进，从另一端出。deque是双端的，左右两边都能进,都能出.
from collections import deque
# mydeque = deque([1,2,3],maxlen=2)# maxlen设置最大长度
# # 当 maxlen 小于已有元素数量时，deque 会自动从左边（头部）丢弃最旧的元素，只保留最后面的 maxlen 个
# print(mydeque)

# mydeque = deque([1,2,3])
# mydeque.append(4)
# print(mydeque)
# mydeque.appendleft(0)
# print(mydeque)
# b = mydeque.pop()
# print(mydeque)
# print(b)
# mydeque.popleft()
# print(mydeque)

# 1.deque.clear() 清空队列，初始化队列长度为1
# mydeque = deque([1,2,3])
# mydeque.clear()
# print(mydeque)

# 2.deque.copy() 创建一个浅拷贝的队列
# mydeque = deque([1,2,3])
# b = mydeque.copy()
# print(mydeque)
# print(b)

# d = deque([[1, 2], [3, 4]])
# d2 = d.copy()

# 方式一：重新赋值元素（改外壳的引用指向）→ 不影响对方
# d2[0] = [999]          # 让 d2[0] 指向一个全新的列表
# print(d)               # deque([[1, 2], [3, 4]])  ← d 没变
# print(d2)              # deque([[999], [3, 4]])

# 方式二：就地修改元素内部（通过引用改对象）→ 会影响对方
# d2[0].append(99)       # 通过共享引用，改了 [1,2] 这个对象本身
# print(d2)
# print(d)               # deque([[1, 2, 99], [3, 4]])  ← d 也被改了！

# 3.deque.count(x) 计算队列中x元素的个数
# mydeque = deque([1,2,3,1,1,1,2,3,5])
# print(mydeque.count(1))

# 4.deque.extend(iterable) 将可迭代对象扩展到队列右边
# deque.extendleft(iterable)将可迭代对象扩展到队列左边
# d = deque([1,2,3])
# # append:整个列表当成一个元素
# d.append([4,5])
# print(d)
# # extend:把列表拆开，逐个加
# d = deque([1,2,3])
# d.extend([4,5,6])
# print(d)

"""注意"""
# # extendleft会将可迭代对象反转过来再添加
# d = deque([1,2,3])
# d.extendleft([4,5,6])
# print(d) # 输出是654123

# 5.deque.index(x) 返回元素x在队列中的位置，没有找到抛出异常ValueError
# d = deque([1,2,3])
# print(d.index(2))

# 6.deque.insert(i, x) 插入元素x到指定位置i。如果位置超出范围，抛出IndexError异常
# d = deque([1,2,3])
# d.insert(1,3)
# print(d)# 输出是1323

# 7.deque.remove(x) 删除第一个找到的元素x，没有元素抛出ValueError异常
# d = deque([1,4,2,3,2])
# d.remove(2)
# print(d)# 输出1432

# 8.deque.reverse() 逆序
# d = deque([1,2,3,4])
# d.reverse()
# print(d)

# deque.rotate(n) 将队列向右移动n个元素，如果n为负数则向左移动n个元素
# d = deque([1,2,3,4])
# d1 = deque([1,2,3,4])
# d.rotate(1)
# print(d)# 输出4123
# d1.rotate(-2)
# print(d1)# 输出3412

# len返回队列长度，为空返回None。
d = deque([1,2,3])
print(len(d))
