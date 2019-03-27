# 工程目录：c:\Users\bin\OneDrive\share\pywork\day08面向对象和过程\03抽象的类的操作.py
# 创建日期: 2019.03.19
# 工程目标：类的相关操作，增加默认的类属性
# 创建作者：binyang
# -*- coding:utf-8 -*-


# 类的属性的增加  将类视为一个具有普遍特性的实例对象
    #实现方式1 在类中直接使用变量名并赋值
    #实现方式2 在类的外面使用类引用对属性赋值

class Money:  #创建类
    #方式1
    
    time = 0
    cord = 20
    key = 30 
    pass

    #类中添加属性方式2 通过类的引用来添加 类名.xxx
Money.count = 1
Money.user = "user1"
 
print(Money.count)
print(Money.__dict__)


# 对类的属性的增删改查 类同对象的属性修改  类名.xxx = xxx
    # 增 通过类中添加属性 通过类名引用增加属性 类名.xxx
    # 删 del 类名.类属性 对象只能删除自己属性，不能删除对象的属性
    # 改  
    # 查  对象先在自己的属性中查找，如果没有就在类的属性张查找

peng = Money()  #创建对象 该对象通过 __class__ 链接到 money 类
print("对象访问类的普遍特点")
print(peng.count)
print(peng.key)
print(peng.time)


# 类的属性的存储问题 使用字典存储 对象属性字典可修改，类属性字典只读，通过气压函数修改
    #在对象的属性中，对象的属性是以字典的方式存储，同样可以通过 peng.__dict__ = {"xxx":xxx...}修改字典的方式添加对象的属性
    
    #在类的属性中是只读的属性，不支持直接修改 ，但是对象中属性可以


# 对象访问 属性的方法
# 可以通过 对象直接赋值 peng = Money()  或者通过 peng.__class_ = Money 来对象实例化
# 先从自己的属性中查找，如果没有从 __class__ 从类中查找，找到后返回



# 类属性属于公共属性，可以被各个对象共享

# 对象的属性，和类属性的联系区别
    # 对象大多是由类实例化而来
    # 类属性绑定在类之中，存储在类中 属性共享给各个对象，抽象层次高，对象不能操作类的属性
    # 类可以实例化各种各样的对象



# 限制对象添加属性的方法
    #通过类属性中的 __slots__限定属性

class Test2:
    __slots__ = ["age"]

    pass

p1 = Test2()
p1.name = "bin" # 报错没有定义
p1.age = 12

print("限制对象属性", p1.age)
#print("限制属性报错",p1.name)





# 类的特殊构造方法 __init__ 该方法在类的实例化的时候会自动调用
# 类的实例化过程会自动调用__init__初始化函数，

class Comple:   # self实质上为类的实例
    def __init__(self, name, age):  #self只是第一个惯例参数的名称，可以使用其他名字
        self.n = name
        self.a = age

x = Comple("yan", 20)
print("自动初始化类函数")
print(x.n, x.a)

class Test:
    def prt(qingqing):
        print(qingqing)
        print(qingqing.__class__)

t = Test()
t.prt()


#类的方法 类的内部使用def 定义方法，类的方法必须包含参数self，且为第一个参数
#self是类的实例

#类定义
class People:
    name = "bin"
    age = 20

    #定义私有属性
    __weght = 170

    #定义构造方法         
    def __init__(self, n, a, w):
        
        self.name = n
        self.age = a
        self.__weght = w
    def Speak(self):
        print("名字：%s, 年龄 ：%s, 身高：%s"%(self.name,self.age,self.__weght))
p = People('qing', 23, 60)
p.Speak()

# 类支持继承，多继承，

#方法重写，如果父类的方法的功能不能满足需求，在子类重写父类的方法