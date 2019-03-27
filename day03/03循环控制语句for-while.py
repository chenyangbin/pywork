# 工程目录：c:\Users\bin\OneDrive\share\pywork\day03\03循环控制语句.py
# 创建日期: 2019.02.26
# 工程目标：循环控制语句Python中的循环语句有 for 和 while。
# 创建作者：binyang
# -*- coding:utf-8 -*-


# while 循环
'''
while 判断语句 ：
    循环语句

注意：同样需要注意冒号和缩进。另外，在Python中没有do..while循环。
'''

# 设定flag 无限循环
'''

falg = 1
while falg == 1:
    num = input("请输入数字")
    print(num)
    '''

# while...else... 转折语句，while的判断FALSE的是时候转而执行else
'''
num = int(input("请输入"))
while num > 10:
    print("num大于十", num)
else:
    print("num小于十", num)
    
'''

# for 语句
'''
for 语句
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

for循环的一般格式如下：
for <variable> in <sequence>:
    <statements>
else:
    <statements>

range() 生成数列的函数，配合for使用，可遍历使用
'''
# break 和 continue
'''
break和continue语句及循环中的else子句
break 语句可以跳出 for 和 while 的循环体。
如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

continue：
continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
var = 10                    # 第二个实例
while var > 0:              
   var = var -1
   if var == 5:             # 变量为 5 时跳过输出
      continue
   print ('当前变量值 :', var)
print ("Good bye!")

pass 语句
Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句，如下实例

'''
