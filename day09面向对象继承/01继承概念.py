# -*- coding: utf-8 -*-
# 创建时间 : 2019/3/27 4:47
# 创建作者: binyang
# 创建目标: 继承简介

#一个类拥另一个类的资源的使用权
#一个类可以继承另一个类的属性和方法，

#类的区分
    #父类 超类 基类
    #子类 派生类 使用父类资源

#类的继承
    #单继承 只继承一个类 从下往上继承 从子类往父类查找
    #多继承  继承多个父类
        #无重叠（属性，方法）的多继承  遵循单调原则，有限按照某个链条深度查找，如果没有换一路径 深度优先
        #有重叠（属性，方法）的多继承

#-----------------------单继承示例-------------------------


class Amianl:
    pass

class Bird:
    pass

class People:
    pass

class Creature(Amianl, Bird, People):  #多继承

    pass
print(Creature.__bases__)  #查看继承的基类

print(type(Creature))
print(Creature.__class__)

class Friend(Amianl): #单继承
    pass

print("不同的方法")
print("各种有限算法")