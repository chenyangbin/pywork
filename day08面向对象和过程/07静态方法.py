# 工程目录：c:\Users\bin\OneDrive\share\pywork\day08面向对象和过程\07静态方法.py
# 创建日期: 2019.03.21
# 工程目标：静态方法的使用和调用
# 创建作者：binyang
# -*- coding:utf-8 -*-


#静态方法不需要第一个默认参数
'''
class jingtai:

    @stticmethod
    def jingtaifnagfa():
        run
        pass
'''

class Person:

    @staticmethod
    def jigntai():

        print("静态方法")
        
Person.jigntai()
p = Person()
p.jigntai()
func = Person.jigntai()


# 三种不同方法访问类和实例属性的权限问题

