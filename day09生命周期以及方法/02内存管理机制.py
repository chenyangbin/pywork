# -*- coding: utf-8 -*-
# 创建时间 : 2019/3/27 1:15
# 创建作者: binyang
# 创建目标: 内存管理机制 引用计数，和垃圾回收

#python皆对象，创建任何变量函数，均会返回对象地址，用于引用

class Person:
    pass
p = Person()

print(p)

#垃圾回收
    #引用计数器：当对象被引用后，每增加一个引用，自身的计数器会加1
    #引用加1的场景
        #对象被创建
        #对象被引用
        #对象被作为参数
        #对象被作为元素存储在容器中



#-----------------------检验引用计数器-------------------------
import sys

class Yin:
    pass

p1 = Yin()  #引用加1 计数为2
print(sys.getrefcount(p)) # 2

p2 = p1 #引用1次
print(sys.getrefcount(p1))

def log(obj):
    print(sys.getrefcount(obj))

log(p2)  #5 此时加2 对象传递给函数的时候，内部有两个引用


# 垃圾回收机制检测流程 从经历过引用计数机制任然没有被释放的对象中找到循环引用干掉相关对象
    #实现机制：
        #找到循环引用>
            #1收集容器对象，可以引用其他对象的对象 通过双向链表引用放在一个表中，
            #2对于有容器的对象通过 “gc_refs" 变量记录当前的引用计数
            #3对于每个容器对象，找到它引用的容器对象，斌将找到的引用对象的引用计数 -1
            # （因为存活在双向链表中的只有两种，一种是真正存在的对象，另一种是相互引用的对象）
            #4引用计数为0的对象可以被回收

    #提升垃圾回收效率底层机制
        #分代回收机制
            #0代每n（一般10通过 gc.set_threshold设置# ）次扫描汇总到1代，激活一次1代和0代同时扫描，同样1代检测n次激活一次同时检测
            #垃圾回收器当中新增的对象的个数，减去消亡的对象的个数差达到移动的阈值会触发垃圾检测


    #垃圾回收时机
        #自动回收
            #满足条件 1开启回收机制， 2达到垃圾回收阈值  通过gc 模块设置 默认开启
                #gc.disable  关闭
                #gc.enable 开启
                #gc.get_threshold 查看参数  返回元组 触发阈值 隔代检测触发值
                #gc.set_threshold 设定参数


        #手动回收
            #手动设置以上参数，来实现内存管理
                #gc.collect
                #
            #手动将循环引用的属性指向none 从而手动解决内存泄漏









