# -*- coding: utf-8 -*-
# 创建时间 : 2019/3/27 3:18
# 创建作者: binyang
# 创建目标:面向对象项目练手

#以面向对象的思想，设计计算器

#思路：将对应的加减乘除方法实现对象

# 计算方法定义为为类方法 封装成一个类

class Caculator:
    result = 0  #类属性

    @classmethod #实现类方法 静态，动态， 类方法  操作类属性，通过类名引用使用类属性
    def first_value(cls, v):

    
        cls.result = v

    @classmethod
    def jiafa(cls, n):
        cls.result += n

    @classmethod
    def jianfa(cls, n):
        cls.result -= n

    @classmethod
    def chengfa(cls, n):
        cls.result *= n

    @classmethod
    def chufa(cls, n):
        cls.result /= n

#该方法的弊端
    #resut 权限不明，容易被修改，故应将result 设为私有属性，只能在类中读取，通过类方法返回即可

Caculator.first_value(2)
Caculator.jiafa(2)
Caculator.chengfa(5)
print("计算结果",Caculator.result)


#-----------------------改良版1 私有属性，增加数据安全-------------------------
#使用私有属性，让属性的权限只在类中放行

class Caculator2:
    __result = 0  #类属性私有化

    @classmethod #实现类方法 静态，动态， 类方法  操作类属性，通过类名引用使用类属性
    def first_value(cls, v):
        cls.__result = v

    @classmethod
    def jiafa(cls, n):
        cls.__result += n

    @classmethod
    def jianfa(cls, n):
        cls.__result -= n

    @classmethod
    def chengfa(cls, n):
        cls.__result *= n

    @classmethod
    def chufa(cls, n):
        cls.__result /= n

    @classmethod
    def Answer(cls):
        print("优化属性结果",cls.__result)

#由于属性的调用 只在该中方法的一个类中，故此版本的计算器不能多开，（只有一个类属性暂存结果）
Caculator2.first_value(5)
Caculator2.chengfa(5)
Caculator2.Answer()


#-----------------------改良版本2，同时多操作该类，将结果绑定为对象属性-------------------------
#不同的计算过程，转化为不同的计算对象，计算过程之间不允许
# 创建类
    #创建对象初始化方法
    #创建计算方法

class Caculator3:

    def __init__(self,num):
        self.__result = num

    def jia(self,n):
        self.__result += n

    def jian(self,n):
        self.__result -=n

    def cheng(self,n):
        self.__result *=n

    def answer(self):
        print("多计算",self.__result)

C1 = Caculator3(2)
C1.jia(5)
C1.answer()



# typ this code in order to test the flames 。so it looks llike beautifu