# 工程目录：c:\Users\bin\OneDrive\share\pywork\day08面向对象和过程\15描述器定义2.py
# 创建日期: 2019.03.24
# 工程目标：描述器的定义方式2 将属性的相关操作封装在对象中  
# 创建作者：binyang
# -*- coding:utf-8 -*-


# 在一个描述器的类中实现三个属性操作方法：set get delete 方法，通过该类创建实例对象，再赋值给其他类的属性中
#-----------------------实质上利用了类来封装属性-------------------------

class Age(object): #封装一个属性类  x新式类描述器才起作用

  def __set__(self, instance, value):
      print(self,instance,value)
      print("set")
      instance.v = value  #绑定在instance 上，每个实例对象才有自己独立的属性，否则绑定在self上则是共享的属性不利于对象属性的独立性
      pass

  def __get__(self, instance, owner):
      print(self,instance,owner)
      print("get")
      return instance.v
      pass

  def __delete__(self, instance):
      print(self,instance)
      print("delete")
      del instance
      pass

class Person(object):  #描述器再新式类起作用
    age = Age() #创建类属性引用该属性是共享的

#    def __getattribute__(self, item): #具有比描述器高的调用优先级
#        print("xxxx")

p = Person()  #创建实例
p2 =Person()  #不同的实例对象具有不同的属性，
p2.age = 11
p.age = 10
print(p.age )

#-----------------------通过类引用访问属性只能调用get 其他方法奴可以-------------------------
'''
print("受限制的类引用访问类属性")
print(Person.age)  #类引用访问
Person.age = 20
del Person.age
'''
#-----------------------描述器优先级-------------------------
#描述器：资料非资料描述器
# 资料描述器：实现了set，get方法
#非资料描述其：只有get方法

#资料描述器>实例属性> 非资料描述器   实现了get，set方法的资料描述器优先级高于实例属性的







