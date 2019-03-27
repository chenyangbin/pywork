# 工程目录：c:\Users\bin\OneDrive\share\pywork\day02\06列表.py
# 创建日期: 2019.02.14
# 工程目标：列表的使用          
# 创建作者：binyang
# -*- coding:utf-8 -*-


# 序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
'''
# Python有6个序列的内置类型，但最常见的是列表和元组
# 列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
# 列表的数据项不需要具有相同的类型
# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可


'''
# 01访问列表元素值

list1 = [1,2,3,4,5,'nihao',"中"]
print("访问元素：list1 的第一个元素，所引0：", list1[6])
print("单独测试：",list1)
for i in range(7):
    print("循环访问测试：",list1[i])


# 02更新列表元素 增删改查
# 改：list[索引下标]

print("原列表：", list1)
list1[6] = 6
print("新列表：", list1)

# 03 删除元素
# 删 del list[索引]
del list1[2]
print("删除第三个元素的新列表：", list1)

# 04 列表的操作符，长度，组合，重复，判断元素存在，迭代访问
'''
Python                  表达式	        结果	描述
len([1, 2, 3])	3	                    长度
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
['Hi!'] * 4	                            ['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
3 in [1, 2, 3]	True	                元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	1 2 3	迭代
'''
# 05 拼接截取
# 拼接
list2 = ['ni', 'hao', 'shijie', 'haha']
list3 = [1, 2, 3, 4, 5, 6, 7]
list4 = list2 + list3  #全拼接
list5 = list3[2:] + list2 # 从第三个元素开始拼接

print(list2)
print(list3)
print("全拼接：", list4)
print("截取拼接：",list5)


# 06嵌套列表
'''
使用嵌套列表即在列表里创建其它列表，例如：

>>>a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
'''

# 07列表操作函数  返回元素个数，返回元素最大值，返回最小值， 将元素不可更改的元组，转换尾列表
'''

Python包含以下函数:
序号	    函数
1	        len(list)       列表元素个数
2	        max(list)       返回列表元素最大值
3	        min(list)       返回列表元素最小值
4	        list(seq)       将元组转换为列表
'''
print("str5的长度：", len(list5))


# 08 列表的相关方法
'''
Python包含以下方法:

序号	方法
1	    list.append(obj)        在列表末尾添加新的对象
2	    list.count(obj)         统计某个元素在列表中出现的次数
3	    list.extend(seq)        在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	    list.index(obj)         从列表中找出某个值第一个匹配项的索引位置
5	    list.insert(index, obj)     将对象插入列表
6	    list.pop([index=-1])        移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	    list.remove(obj)        移除列表中某个值的第一个匹配项
8	    list.reverse()          反向列表中元素
9	    list.sort(cmp=None, key=None, reverse=False)    对原列表进行排序
10	    list.clear()            清空列l表
11	    list.copy()             复制列表


'''

list5.append('89')
print("append 在末尾插入元素：",list5)

