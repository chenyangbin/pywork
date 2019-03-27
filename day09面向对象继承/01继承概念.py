# -*- coding: utf-8 -*-
# 创建时间 : 2019/3/27 4:47
# 创建作者: binyang
# 创建目标: 继承简介

#一个类拥另一个类的资源的使用权
#一个类可以继承另一个类的属性和方法，

#类的区分
    #父类 超类 基类
    #子类 派生类 使用父类资源

#继承涉及的问题
    #1继承资源的权限 可使用的资源  
    #2继承资源的使用 多继承的时候资源选择 
    #2继承资源的覆盖 多继承的时候资源优先级的选择
    #4资源的累加     继承资源后，增加功能


#---------------继承资源权限 公有 受保护 私有 ----------------
#属性和类的权限 
# 公有属性， 类中变量
# 私有属性， _
# 受保护的属性 __

#1测试子类对父类的权限的继承
class Author_futher:
    #属性权限
    a = 1
    _b = 2
    __c = 3

    #方法权限
    def t1(self):
        print("t1")

    def _t2(self):
        print("t2")

    def __t3(self):
        print("t3")

    def __init__(self):  #内置方法
        print("init") 

class Test(Author_futher):
    def test(self):
        print(self.a)
        print(self._b)
        print(self.__c) 
    
        self.t1()
        self._t2()
        self.__t3()
        self.__init__()

p = Test()  #创建对象
p.t1()
p._t2()
p.__t3() # 类同属性的权限  私有属性，和私有方法都不能访问




#类的继承型态
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

class Creature(Bird, People):  #多继承
    pass

print(Creature.__bases__)  #查看继承的基类

print(type(Creature))
print(Creature.__class__)

class Friend(Amianl):
    def __init__(self):
        pass
    
    pass





#---------------继承资源调用的查找顺序 ----------------

#单继承：从下往上，从子往父查找

#无重叠继承：单调原则
    #先左侧继承链，再右侧

#有重叠多继承：
    #python27
    




#由于搜索排序的模式的不同，导致，在属性的使用的使用的时候
#继承的顺序按照python的版本的不同，以及使用的算法和侧重点不同，顺序也不同#
