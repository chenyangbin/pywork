# 工程目录：c:\Users\bin\OneDrive\share\pywork\day03\04迭代器和生成器.py
# 创建日期: 2019.02.26
# 工程目标：迭代器和生成器
# 创建作者：binyang
# -*- coding:utf-8 -*-
import sys

# 迭代器
'''
访问集合元素的一种方式，可以记住变量位置的对象，
迭代器从集合的第一个元素开始访问直到所有的元素，迭代器只能前进不能后退
迭代器的两个方法。iter（），next（）
字符串，列表，元组都能创建迭代器
'''

# 迭代访问示例iter（）
'''
list1 = [1, 2, 3, 4, 6, 8]
it = iter(list1)
for a in it:
    print(a, end='  ')
'''

# 迭代访问示例 next（）
'''
list2 = [1, 2, 2, 3, 4, 5, 6, 7, 9]
it = iter(list2)
while True:
    try:
        print(next(it))
    except StopIteration:
        pass
'''

#  通过类实现迭代
'''
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。

__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法
并通过 StopIteration 异常标识迭代的完成。

__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
'''
'''
class Mynums:
    def _iter_(self):
        self.a = 1
        return self

    def _next_(self):
        x = self.a
        self.a += 1
        return x

myclass = Mynums()
myiter = iter(myclass)

print(next(myiter))


'''

# stoplteration 标识迭代完成


# 生成器 yield函数
'''
在 Python 中，使用了 yield 的函数被称为生成器（generator）。

跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，
更简单点理解生成器就是一个迭代器。

在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

调用一个生成器函数，返回的是一个迭代器对象。
打个比方的话，yield有点像断点。     加了yield的函数，每次执行到有yield的时候，
会返回yield后面的值 并且函数会暂停，直到下次调用或迭代终止；
'''

