# 工程目录：c:\Users\bin\OneDrive\share\pywork\day08面向对象和过程\12面向对象特殊属性.py
# 创建日期: 2019.03.22
# 工程目标：内置特殊属性了解
# 创建作者：binyang
# -*- coding:utf-8 -*-


#python中内置的特殊的属性相关
#---------------类属性 系统自动分配----------------
'''
__dict__:类的属性
__bases__:类的索引的父类构成元组
__doc__:类的文档字符串
__name__:类名
__module__: 类定义所在的模块
'''
class Person:
    '''
    doc示例 文档
    '''
    age = 19
    def __init__(self, *args, **kwargs):
        self.name = "qing"
        #return super().__init__(*args, **kwargs)
    pass

    def run(self):
        print("run")

print("显示类的属性",Person.__dict__)
print("显示类的元组",Person.__bases__)
print("显示类的文档字符",Person.__doc__)
print("显示类的类名",Person.__name__)
print("显示类的所属模块", Person.__module__)


#---------------实例属性----------------
'''
__dict__": 实例属性 字典的形式显示所有属性
__class__: 实例对应的类 
'''