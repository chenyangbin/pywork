# 工程目录：c:\Users\bin\OneDrive\share\pywork\day08面向对象和过程\06面向对象-类方法.py
# 创建日期: 2019.03.21
# 工程目标：类方法的使用以及调用
# 创建作者：binyang
# -*- coding:utf-8 -*-


#类的调用

'''
类方法的语法和调用
语法
class Lei:
    @classmethod
    def run():
        pass

'''
class Lei:
    @classmethod
    def eat3(cls,food):
        print("吃", cls, food)

#类调用
Lei.eat3(222)
#类调用2
func = Lei.eat3
print(func(555))

#实例调用
p = Lei()
p.eat3(333)


#衍生类的调用 使用了原生类的各种方法

class a(Lei):
    def __init__(self ):
        pass

a.eat3(444)