# -*- coding:utf-8 -*- 
#创建日期：2019.03.28
#创建路径：c:\Users\bin\OneDrive\share\pywork\day09面向对象继承\022.3-3版本-c3算法.py
#创建作者：binyang
#创建目标：python2至pytho3的版本中继承所用C3算法



#--------------------C3算法·--------------------
#出现缘由：解决前MEO算法中的深度优先，广度优先不足   DFS:深度优先 BFS：广度优先
#实现过程，
### 如果第一个序列的第一个元素，是后续序列的第一个元素，或者不在后续序列中再次出现，则将这个元素合并到最终的方法解析顺序序列中，并从当前操作的全部序列中删除。
### 如果不符合，则跳过此元素，查找下一个列表的第一个元素，重复1的判断规则

#--------------------菱形继承--------------------
# A->BC B->D   C->D

class D(object):
    #    最终序列   父类访问顺序      所有父类列表
    # L(D) = [D] + merge(L(object), [object])  本身集合 +            + 所有父类集合
    #      = [D] + merge([boject],[object])
    #      = [D] + merge([],[]) 判定
    #      = [D,object]
    pass

class B(D):
    # L(B) = [B] + merge( L(D)， [D] )
    #      = [B] + merge( [D,object], [D] )       
    #      = [B + D ] + merge( [object], [] ) 
    #      = [B + D] +  merge([object])
    #      = [B, D, object]
    pass
    # L()
class C(D):
    #L(c) = [c] + merge(L(B), [B])
    #     = [c] + merge([B, D, object], [B])
    #     = [c] + merge([D, object], [])
    #     = [c, B] + merge([D, object])
    #     = [c, B, D, object] + merge([])
    #     = [c, B, D, object]
    pass

class A(B,C):
    #L(A) = [A] + merge(L(B), l(C), [B, C])
    #L(A) = [A] + merge([B, D, object],   [c, B, D, object],  [B, C]) #判定首元素B是不是，后续所有元素的首元素 不是则按照同样的判定方法判定写一个列表，判断下一个
    #L(A) = [A] + merge([B, D, object],   [c, B, D, object],  [B, C]) 
    pass

#金典类深度优先 ABDC的顺
#import  inspect
# print "深度优先算法的解析路径" 
#print inspect.getmro(A)  #打印结果(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <type 'object'>)































