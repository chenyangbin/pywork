# 工程目录：c:\Users\bin\OneDrive\share\pywork\day08面向对象和过程\11面向对象只读属性.py
# 创建日期: 2019.03.21
# 工程目标：面向对象只读属性
# 创建作者：binyang
# -*- coding:utf-8 -*-

#只读属性，即属性只能读取不可以修改

#应用场景，有的属性只能在内部修改，外部只能读取不能修改 比如电脑的网络状态

#---------------只读属性的实现方式1----------------
#通过属性前双下划线实现私有化的既不能读也不能写，而后通过公开的方法实现读操作
class Person:

    def __init__(self, *args, **kwargs):
        self.__age = 10
        #return super().__init__(*args, **kwargs)

    def Getage(self):  #通过内部访问属性
        return self.__age

p1 = Person()
#print("读取属性", p1.__age)  #私有化以后类外部无法访问，只能通过内部访问
print(p1.__dict__)  #通过它查看私有化受的属性实际上是 _Person__age
print(p1.Getage())  #通过内部调用返回访问，完成读操作

p1.age = 10  # 外界尝试赋值的时候实际上是添加了新的属性
print(p1.__dict__)  #查看实际上添加的属性

#---------------解决属性只读的麻烦，（只能通过调用的方式） 使用 @property解决----------------

class Person1:
    
    def __init__(self, *args, **kwargs):
        self.__age = 10
        #return super().__init__(*args, **kwargs)

    #此处使用property装饰器
    @property
    def Getage(self):  #通过内部访问属性
        return self.__age

p2 = Person1()
print("使用perproty 装饰器解决", p1.Getage)  #直接访问 不加调用

#尝试赋值的时候会报错
p2.age = 20 #报错
#p1.age = 20
#print("写入后读取",p1.age)

