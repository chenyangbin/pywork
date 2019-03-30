# -*- coding:utf-8 -*- 
#创建日期：2019.03.30
#创建路径：c:\Users\bin\OneDrive\share\pywork\day13异常处理\03contexlib模块.py
#创建作者：binyang
#创建目标：上下文模块


#提供一些的函数
'''
创建上下文管理实际就是创建一个类，添加__enter__和__exit__方法,
Python标准库还提供了更加易用的上下文管理器工具模块contextlib，
它是通过生成器实现的，我们不需要再创建类以及__enter__和__exit__这两个特俗的方法：
'''
'''
from contextlib import contextmanager

@contextmanager #装饰器
def make_open_context(filename, mode):
    fp = open(filename, mode)
    try:
        yield fp

    finally:
        fp.close

#with make_open_context()
with make_open_context('/tmp/a.txt', 'a') as file_obj:
    file_obj.write("hello carson666")

'''
#contextlib.close
#--------------------contexlib.close--------------------
#使不是上下文管理器的对象变成上下文管理器

#常规方法实现上下文管理功能
class Test:
    def t(self):
        print("测试语句")

    def close(self):
        print("资源释放")

    def __enter__(self):
        return self

    def __exit__(self):
        self.close(self)
        
import contextlib #使用该库快速实现上下文资源管理
with contextlib.closing(Test()) as t_obj:
    t_obj.t()
