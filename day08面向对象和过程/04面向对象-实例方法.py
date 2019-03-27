# 工程目录：c:\Users\bin\OneDrive\share\pywork\day08面向对象和过程\04面向对象-方法.py
# 创建日期: 2019.03.19
# 工程目标：面向对象方法要点
# 创建作者：binyang
# -*- coding:utf-8 -*-


# 面向对象中的方法的关键点 方法的概念 方法的划分 方法的实例 类的方法 静态的方法 相关补充

# 定义在类中的具有某种功能的函数
# 方法的概念
    # 定义在类或者对象中的一个实现具体功能的函数  描述一个目标或者行为动作
    # 和函数类似
        #封装一系列的指向动作，可以调用，主要区别是调用方式

#函数的调用
def test(num):
    print(num)

#调用方法
class test3:
    def fangfa(self):
        print(self)


p = test3()
p.fangfa()  #调用




#方法的划分 根据方法的接受的第一个参数的数据类型
    #实例方法 默认第一个参数接收的是一i个实例
    #类方法 默认第一个参数接收的是一个类
    #静态方法 第一个参数什么也不默认接收
class Person:

    def eat(self): #实例方法
        print("实例方法",self)
    
    @classmethod #类方法
    def leifangfa(self):
        print("类方法",self)
        #raise NotImplementedError

    @staticmethod  #静态方法
    def jingtaifnagfa():
        print("静态方法")
        pass
p = Person()
p.eat()  #实例方法
print(p)  #实例方法
# 类方法
Person.leifangfa()  #默认第一个参数是实例类
# 静态方法
Person.jingtaifnagfa()


# 类对象和实例对象的存储位置
print("实例对象",p.__dict__)  #实例对象
print("类对象", Person.__dict__, end='\n')  #类对象
    # #由打印的内容可以看出
    # '''
    # 实例对象 {}
    # 类对象 {'__module__': '__main__',
    #        'eat': <function Person.eat at 0x000001AAB8029AE8>,
    #        'leifangfa': <classmethod object at 0x000001AAB8034278>, 
    #        'jingtaifnagfa': <staticmethod object at 0x000001AAB8034240>, 
    #        '__dict__': <attribute '__dict__' of 'Person' objects>, 
    #        '__weakref__': <attribute '__weakref__' of 'Person' objects>, 
    #        '__doc__': None}  是个字典
    #  '''

# 不同的类的方法的调用
'''
实例方法
class Person:
    def run(self):  #第一个形参表示以后接收的第一个参数是实例本身
        pass
'''
class Qing:
    def eat(self,foood): 
        print("好吃，嗯", self, foood)
    
        
Q = Qing()
Q.eat("红薯")  #使用实例方法的时候，可以不用self参数，解释器自动填写
Q.eat(9999, "棒棒糖")  #第一个参数也可以传值
print(Q)
'''打印结果  self是Q实例本身
好吃，嗯 
<__main__.Qing object at 0x000001E94EA7C278> 
红薯
<__main__.Qing object at 0x000001E94EA7C278>
''' 



