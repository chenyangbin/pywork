# 工程目录：c:\Users\bin\OneDrive\share\pywork\day08面向对象和过程\10面向对象的私有化属性.py
# 创建日期: 2019.03.21
# 工程目标：私有化属性
# 创建作者：binyang
# -*- coding:utf-8 -*-


#属性的访问权限问题
#私有化属性让类的属性只可以在类的内部可以访问，外部无法访问，保证数据的安全性

#---------------属性权限分类----------------
'''
X公有属性权限
    类的内部访问 可以
    子类内部访问 可以
    模块内部其他位置访问  可以


    跨模块访问  可以
        import 导入
        from 模块 import * 导入

'''
class Animal:
    x = 10
    def test(self):
        print(Animal.x)  #类内部访问
        print(self.x)
    pass

class Dog(Animal):
    def test(self):
        print(Dog.x)
        print(self.x)
    pass

a = Animal()  #生成实例化a
b = Dog()      #生成实例化b

a.test()    #类访问
b.test()  #子类访问

a = 666  #在别的模块中（py文件）通过import 导入该文件就可以访问该文件源码中的函数变量



#---------------  _y 受保护的属性   ----------------
'''
受保护的属性权限
    类内部的访问 可以
    子类内部的访问 可以

    模块其他位置访问 警告
        类访问 警告
        实例访问 警告

    跨模块访问 (在其他文件导入访问)
        import 形式 告警受保护
        fron module import * 形式导入  
            有 _all_ 指明对应变量 告警
            没有 _all_ 指明对应变量 报错

'''
class Animal1:
    _x = 100
    def test1(self):
        print("受保护的属性内部",Animal1._x)  #类内部访问
        print("受保护的属性内部",self._x)
    pass

class Dog1(Animal1):
    def test1(self):
        print("受保护的属性子类访问",Dog1._x)
        print("受保护的属性子类访问",self._x)
    pass

a = Animal1()  #生成实例化a
b = Dog1()      #生成实例化b

a.test1()    #类访问
b.test1()  #子类访问

print("受保护的属性其他位置的类访问",Animal1._x)  #允许 警告
print("受保护的属性其他位置的子类访问", Dog1._x)  #允许 警告

#跨模块 导入import 访问
#在被导入的文件模块中使用 __all__ = {"_a","其他变量"} 表示其他模块可使用列表中的变量


a = 666  #在别的模块中（py文件）通过import 导入该文件就可以访问该文件源码中的函数变量
         #访问限制是 被导入模块要被访问的变量必须使用 __all__ = {"xx","xx"} 提前声明





#--------------- __z 受保护的私有属性(两个下划线) 权限 ----------------
'''
只能在类的内部访问，其他位置，，都不可以访问
伪私有，防止外界访问，




'''
class Animal2:
    __x = 1000
    def test2(self):
        print("受保护的属性内部",Animal2.__x)  #类内部访问可以
        print("受保护的属性内部",self.__x)
    pass

class Dog2(Animal2):
    def test2(self):
        print("受保护的属性私有子类访问",Dog2.__x)  
        print("受保护的属性私有子类访问",self.__x)
    pass

a = Animal2()  #生成实例化a
#b = Dog2()      #生成实例化b

a.test2()    #类访问 可以
# b.test2()  #子类访问 不可以

# print("受保护的私有属性其他位置的类访问",Animal2.__x)  #不可以 警告
# print("受保护的私有属性其他位置的子类访问", Dog2.__x)  #不可以 警告






#---------------私有化属性的应用场景----------------
#python中斌没有真正的属性私有化 通过下划线的数量实现私有化 

'''
数据保护，数据限制
_x 只能在类和子类访问

__x只能在类中访问

'''

class Person:
    
    #初始化实例方法，使用该方法，只要用于初始化其他实例的属性的默认值，
    #在创建实例对象后，会借用该方法中的属性值，用于初始化其他对象的属性初始化值，但不会影响其自身的值的设定
    def __init__(self, *args, **kwargs):
        self.age = 18
        self.hight = 170
        self.sex = None
        #return super().__init__(*args, **kwargs)

p1 = Person()

p2 = Person()

print("自动初始化参数", p1.age, p1.hight, p1.sex)

p2.sex = "boy" #修改默认的初始化参数
print("自动初始化参数其中sex自定义", p2.age, p2.hight, p2.sex)