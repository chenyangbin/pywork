# -*- coding:utf-8 -*- 
#创建日期：2019.03.30
#创建路径：c:\Users\bin\OneDrive\share\pywork\day09面向对象多态\01多态.py
#创建作者：binyang
#创建目标：多态

#指，一个类的多种形态
#调用是的多种形态产生多种结果形

#不同的对象，调用相同的方法，产生多种形态结果

#示例

class Animal(object):

    def jiao(self):
        pass

class Dog(Animal):
    def jiao(self):
        print("wang")


class Cat(Animal):
    def jiao(self):
        print("miao")


def test(obj):

    obj.jiao()

11119