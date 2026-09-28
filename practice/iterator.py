# 练习 day7：迭代器
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
# 迭代器可以存储无限多的数据，但是数据容器不可以
from collections.abc import Iterator
print(isinstance([],Iterator))

print(isinstance(iter([]),Iterator))
print(isinstance(iter('abc'), Iterator))
