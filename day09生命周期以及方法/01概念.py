# -*- coding: utf-8 -*-
# 创建时间 : 2019/3/26 23:23
# 创建作者: binyang
# 创建目标: 对象的生命周期

# 对象在程序的运行的过程中在程序中运行释放的时间段
#当对象不再使用，节约内存，释放对象

#掌控一个对象
#监听对象的生命周期
    #__new__ 方法  用于给对象分配内存， 通过拦截该过程可以修改对象的创建过程。

    #__init__ 方法 用于初始化对象的参数

    #__del__ 对象的释放方法  当对象被释放，会自动调用该方法


#-----------------------监视对象-------------------------

class Person:
    def __new__(cls, *args, **kwargs):  #拦截对象的创建过程

        pass

    def __init__(self):  #自动调用该方法初始化初始创建的对象

        pass

    def __del__(self):  #释放对象后自动调用该对象
        pass
    pass

p1 = Person()
print(p1)

#-----------------------统计一个类创建实例的数量状态-------------------------
n = 0
class Person1:
    #n = 0
    def __init__(self):
        global n
        n+=1
        print("创建对象",n)
        #return  n

    def __del__(self):
        global n
        n-=1
        print("删除对象",n)
        #return n
    def __new__(self):
        pass



p2 = Person1()  #创建一个对象
p3 = Person1()  #创建对象一次
p4 = Person1()  #创建对象
print("当前数量",n)
del  p4
print("当前对象数量",n)

