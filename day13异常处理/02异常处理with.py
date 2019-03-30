# -*- coding:utf-8 -*- 
#创建日期：2019.03.30
#创建路径：c:\Users\bin\OneDrive\share\pywork\day13异常处理\02异常处理with.py
#创建作者：binyang
#创建目标：异常处理-with 资源访问


#python异常之with

#with 常用场景        
# 数据库连接,锁分配,信号量加减状态管理,打开/关闭文件,异常处理,等等.

# 基本语法
'''
with expression [as target]:
with_body
'''

#参数说明：
'''
expression：是一个需要执行的表达式；
target：是一个变量或者元组，存储的是expression表达式执行返回的结果，可选参数。
'''

#eg: 例子,打开文件
'''
with open('d:\\tmp:\\test1.txt','r') as fp:
      pass
'''
# 异常处理特点 with
'''
with仅能工作于支持上下文管理协议(context managementprotocol)的对象
支持这种协议的有：
􀁺 file
􀁺 decimal.Context
􀁺 thread.LockType
􀁺 threading.Lock
􀁺 threading.RLock
􀁺 threading.Condition
􀁺 threading.Semaph
􀁺 threading.BoundedSemaphore
open()中产生的异常不能捕获
with只能捕获pass部分的异常
'''

# with处理异常原理：
'''
（1）__enter__
     __exit__:
with不管什么情况都会执行这两个方法，所以使用with处理的对象必须有__enter__()和__exit__()
其中__enter__()方法在语句体（with语句包裹起来的代码块）执行之前进入运行
    __exit__()方法在语句体执行完毕退出后运行。

（2）with语句的工作原理：
紧跟with后面的语句会被求值，返回对象的__enter__()方法被调用，这个方
法的返回值将被赋值给as关键字后面的变量，当with后面的代码块全部被执
行完之后，将调用前面返回对象的__exit__()方法。
'''

#with处理适用场景
'''
    with 语句适用于对资源进行访问的场合，
    确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源
    比如文件使用后自动关闭、线程中锁的自动获取和释放等。
    因为上下文管理器主要作用于共享资源,你可以想象到__enter()__和__exit()__方法基本是干的需要分配和释放资源的低层次工作

    比如:
        数据库连接,
        锁分配,
        信号量加减
        状态管理,
        打开/关闭文件,
        异常处理,等等.

'''

#自定义with异常
class opened(object):
    def __init__(self,fileName):
        self.handle=open(fileName)
    def __enter__(self):
        print 'enter method'
        return self.handle
    def __exit__(self, exc_type, exc_val, exc_tb):
# 异常的类型，异常的值，异常的堆栈信息
if exc_tb is None:
    print 'No Exception'
    self.handle.close()
else:
    print 'type',exc_type
    print 'value',exc_val
    print 'tb',exc_tb
    self.handle.close()
    return False
 
with opened('d:\\tmp\\test1.txt') as fp:
for line in fp.readline():
    print line
raise Exception('bad input')


