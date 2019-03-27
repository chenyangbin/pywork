
# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\14装饰器的使用.py
# 创建日期: 2019.03.11
# 工程目标：装饰器的使用 在函数名以及函数体不变的前提下，给函数附加一些额外的代码
# 创建作者：binyang
# -*- coding:utf-8 -*-


# 装饰器：将一个函数镶嵌在另一个函数中，进行重复使用的母的
# 语法
'''
    1 定义不同功能的函数  代码功能和业务逻辑分离 提高代码的重用性能 方便代码的维护

    2  

'''




# 根据不同的业务逻辑层调用不同的代码

# 当有新的业务逻辑的需求的时候，添加代码的方式
'''
    1直接在业务逻辑中添加 麻烦 冗余度大 维护性能差
    
    2直接在功能函数中修改 影响了功能函数的功能独立 ，及一个函数的单一职责

    3装饰器调用
'''



''' 方式1
 # 方式1  基础函数功能加业务逻辑函数 添加功能在其他功能函数中调用

 # 登陆验证函数

def sendsuosuo():
    print("发说说")

    return 0

def sendimg():
    print("发图片")

    return 0
def checklogin(func): # 函数的功能参数中传入函数
    print("登陆验证")
    func()

btnindex = 2
 
if btnindex == 1:
    checklogin(sendsuosuo) #登陆验证
    sendsuosuo()  
else:
    checklogin(sendimg)    # 登陆验证中调用其他函数，影响函数功能的单一性
    #sendimg()

'''

''' 方式2 python实现装饰器
# 方式2 在不改变缘由函数功能9定义的条件下，增加业务逻辑功能
 # 登陆验证函数
def checklogin(func):  # 函数的功能参数中传入函数
    def inner():        # 封包操作 把登陆操作 装饰新的功能
        print("登陆验证")  
        func()
    return inner

def sendsuosuo():
    print("发说说")
    return 0
sendsuosuo = checklogin(sendsuosuo)  #新的功能函数封包传给新的变量 使用checklogin来间接调用其他功能函数

def sendimg():
    print("发图片")
    return 0

sendimg = checklogin(sendimg)

btnindex = 2 # 功能切换标志

 
 # 在保证业务逻辑不变的清空下，添加额外的代码功能
 # 业务逻辑
if btnindex == 1:
    sendsuosuo()   # 基础业务逻辑代码不变
else:  
   sendimg()



'''

# python 装饰器的语法糖，简洁操作
 # 登陆验证函数
def checklogin(func):  # 函数的功能参数中传入函数
    def inner():        # 封包操作 把登陆操作 装饰新的功能  用内部函数调用其他函数的功能，不干扰其他函数
        print("登陆验证")  
        func()
    return inner

@checklogin # 语法糖简洁操作 ，相当于109
def sendsuosuo():
    print("发说说")
    return 0
#sendsuosuo = checklogin(sendsuosuo)  #新的功能函数封包传给新的变量 使用checklogin来间接调用其他功能函数

@checklogin  # 语法糖简洁操作相当于116行
def sendimg():
    print("发图片")
    return 0

#sendimg = checklogin(sendimg)

btnindex = 2 # 功能切换标志

 
 # 在保证业务逻辑不变的清空下，添加额外的代码功能
 # 业务逻辑
if btnindex == 1:
    sendsuosuo()   # 基础业务逻辑代码不变
else:  
   sendimg()

# 装饰器的运行顺序，从上至下

def zsq(func3):     #装饰器的调用要传入内封函数名
    def inner2():            
        print("装饰器执行")
        func3()     # 调用内部函数pnum一次
    return inner2

@zsq #功能相当于 pnum = zsq(pnum) 相当于把运行的逻辑功能函数带入带入到定义装饰器的函数中
def pnum():
    print(20)

pnum()


# 装饰器装饰有参数函数的使用 装饰器传参 装饰器实际调用
def zsqcc(func3):     #装饰器的调用要传入内封函数名
    def inner3(n1): #内部函数，参数名不受外部影响           
        print("装饰器传参执行")
        func3(n1)     # 装饰器实际调用最终函数一次 故传入参数和调用参数应保持一致
    return inner3

@zsqcc #功能相当于 pnum = zsq(pnum) 相当于把运行的逻辑功能函数带入带入到定义装饰器的函数中
def pnum2(num):
    print(num)

pnum2(123)


# 装饰器的不定长 传参 使用 元组，字典传参 传参的习惯性关键字 列表传参：*args  字典关键字传参 ：**kwargd
# 装饰器的不定长 传参示例
def zsqcc_bdc(func4):     #装饰器的调用要传入内封函数名
    def inner3(*args, **kwargs):  #内部函数，参数名不受外部影响
        print("="*20)          
        print("装饰器的不定长",args, kwargs)
        func4(*args, **kwargs)     # 装饰器实际调用最终函数一次 故传入参数和调用参数应保持一致  参数调用拆包
    return inner3

@zsqcc_bdc #功能相当于 pnum = zsq(pnum) 相当于把运行的逻辑功能函数带入带入到定义装饰器的函数中
def pnum3(num1,num2,num3):
    print("装饰器不定长传参使用",num1,num2,num3)

# 对于装饰器装饰过（内部封装后）的函数格式，可以多次调用张诗琪的功能 
    
 
pnum3(123, 456, num3=666)


# 关于装饰器的内部的函数 的返回值的问题 保证调用和函数定义的返回值一致
def zsqcc_fhz(func5):     #装饰器的调用要传入内封函数名
    def inner6(*args, **kwargs):  #内部函数，参数名不受外部影响
        # 保证inner内部函数和调用的函数的结构一致
        print("="*20)          
        print("装饰器返回值0",args, kwargs)
        result6 = func5(*args, **kwargs)  # 装饰器实际调用最终函数一次 故传入参数和调用参数应保持一致  参数调用拆包
                                          # func5实际调用pnum5和pnum6 故调用完毕后要返回结果必须对结果保存
        return result6                    # 调用函数返回结果
    return inner6

@zsqcc_fhz #功能相当于 pnum = zsq(pnum) 相当于把运行的逻辑功能函数带入带入到定义装饰器的函数中
def pnum5(num4,num5,num6):
    print("装饰器返回值1", num4, num5, num6)
    return num4 + num5
    
@zsqcc_fhz  # @后视为一个函数

def pnum6(num7):
    print("装饰器返回值2")

# 对于装饰器装饰过（内部封装后）的函数格式，可以多次调用装饰器的功能 
    
 
res1 = pnum5(123, 456, num6=666)
res2 = pnum6(222)

print("调用函数的最终返回值",res1)
print("调用的时候在pum6中没有使用返回值", res2)

'''
def zsqcc2(func6):  #func6传递了f1 等同于f1
    def inner(*args, **kwargd):
        print("装饰器带参数") # 此处执行附加的其他功能
        

        func6()  # 此处执行调用函数
        result9 = func6(*args, **kwargd)  #保存返回调用函数的结果
        return result9  # 返回调用结果
    return inner # 返回调用函数到上一层
'''

#装饰器中带参数（调用附加的不同功能）的装饰器
def zsq_diffuc(dffunc):
    def inner():
        print("*" * 20)
        dffunc()
    return dffunc



