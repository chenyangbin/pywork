
# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\15迭代器.py
# 创建日期: 2019.03.17
# 工程目标：生成器的使用
# 创建作者：binyang
# -*- coding:utf-8 -*-


# 生成器 遍历数据 惰性迭代 节省内层空间 字典记录遍历状态 next直接按顺序下一个访问
# 特点：
#   1惰性计算数据 节省内存
#   2记录 状态，通过next访问下一个状态
#   3具备可迭代特性 生成器具有迭代器特性，但迭代器不是生成器
# 创建方式：
#   1把列表的表达：{}  修改 为[] 即可  表达式，非元素

#示例：

l = [i for i in range(1, 100) if i % 2 == 0]  #表达式形式的列表

l2  = (i for i in range(1, 100) if i % 2 == 0) # 生成器形式的列表

print("表达式形式列表", l)
print("生成器形式列表", l2)

# 访问生成器中的数据（特殊的迭代器）
print("生成器访问列表", next(l2))
print("生成器访问列表", next(l2))
print("生成器访问函数方法", l2.__next__())

# 生成器创建方式2 函数中包含yield语句 函数的执行结果就是生成器
#   特点：
#   1 yield 可以阻断当前程序的执行 ，然后当使用next函数的时候，或者_next_ 函数的时候，
#     都会让函数继续执行，直到下一个yield又会被暂停

def test():
    print("xxxx")
    yield 1
    #print(1)
    print("aa")

    yield 2
    print(2)

    yield 3
    print(3)

g = test()   # 只有在使用next 或者_next_才可以访问，仅仅调用不会执行生成器
print(" 创建生成器方式2",g)
print(" 创建生成器方式2", next(g))
print(" 创建生成器方式2", next(g))  # 只有在




# 生成器 产生数据的方式，让生成器生成数据
    # 1 next
    # 2_nxet_
    # 3 for in

# 生成器的操作方法
# 1 send 方法 有一个参数，指定的是上一次被刮起的yield的语句的返回值
# 2 可以给额外的yield的语句赋值
# 3 之一第一次调用的时候 t.send(none)

def test2():
    print("xxxxxx")
    res1 = yield 1   # 第一次yield 而后挂起
    print(res1)


    res2 = yield 2 # 第二次执行yield 
    print(res2)

g1 = test2()  # 此时不打印xxx 不启动函数的调用
print("生成器的操作",g1.__next__())
#print("生成器的操作", g1.__next__()) 第二次执行yield  
print("生成器的操作使用send给yield赋值", g1.send("oooo"))  # send方法可以给yield赋值 传值给上一次挂起的yield

# 关闭生成器方法  close

def cose_scq():
    yield 1
    print("a")

    return 10 # 运行到此处以后就会结束运行  抛出异常
    yield 2
    print("b")

    yield 3 
    print("c")
a =cose_scq()

print(a.__next__())

print(a.__next__())
print("关闭生成器")

a.close()  #  关闭生成器

#生成器已经关闭 print(a.__next__())

# 注意，生成器的迭代器使用一次迭代完毕以后，就不能再次使用了，除非再次调用生成器迭代，即生成器只能遍历一次