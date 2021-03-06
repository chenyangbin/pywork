# 工程目录：c:\Users\bin\OneDrive\share\pywork\day02\运算符.py
# 创建日期: 2019.02.11
# 工程目标：python 运算符 加减乘除 大小相等 与或非 and/or/not  in/not in   is/is not   
# 创建作者：binyang
# -*- coding:utf-8 -*-


# 算术运算符 加，减，乘，除，模（% 取余），幂（**），取整（//）
'''
假设 a = 10 b = 21
运算符	描述	                                实例
+	    加 - 两个对象相加	                             a + b 输出结果 31
-	    减 - 得到负数或是一个数减去另一个数	               a - b 输出结果 -11
*	    乘 - 两个数相乘或是返回一个被重复若干次的字符串	    a * b 输出结果 210
/	    除 - x 除以 y	                                 b / a 输出结果 2.1
%	    取模 - 返回除法的余数	                           b % a 输出结果 1
**	    幂 - 返回x的y次幂	                              a**b 为10的21次方
//	    取整除 - 向下取接近除数的整数	                     >>> 9//2  4

'''

# 比较运算符  等于 ==， 不等于！=， 大于：>, 小于等于:<=,   返回值。真假 true false
'''
假设 a=10 b=20 

运算符      描述                                   示例 
==          等于-比较左右值是否相等                 
!=          不等于-比较左右值是否不相等
>           大于-比较左值是否大于右值
<           小于-比较左值是否小于右值
>=          大于等于-比较左值是否大于等于右值
<=          小于等于-比较左值是否小于等于右值
'''


# 赋值运算符：
'''

运算符	 描述	            实例
=	    简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
+=	    加法赋值运算符	    c += a 等效于 c = c + a
-=	    减法赋值运算符	    c -= a 等效于 c = c - a
*=	    乘法赋值运算符	    c *= a 等效于 c = c * a
/=	    除法赋值运算符	    c /= a 等效于 c = c / a
%=	    取模赋值运算符	    c %= a 等效于 c = c % a
**=	    幂赋值运算符	    c **= a 等效于 c = c ** a
//=	    取整除赋值运算符	c //= a 等效于 c = c // a

'''

# 位运算符：与：& （按位与），  或： 非
'''
a=60 b=13
&	按位与运算符：  参与运算的两个值,如果两个相应位同1,则为1,否则为0	                                (a & b) 输出结果 12 ，二进制解释： 0000 1100
|	按位或运算符：  只要对应的二个二进位有一个为1时，结果位就为1。	                                    (a | b) 输出结果 61 ，二进制解释： 0011 1101
^	按位异或运算符：当两对应的二进位相异时，不同时候，结果为1	                                        (a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1	                     (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
<<	左移动运算符：  运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	    a << 2 输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符：  把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数	               a >> 2 输出结果 15 ，二进制解释： 0000 1111

'''
print("-----位运算符-----")
a = 60
b = 13

print("二进制表示a=60，b=13：",bin(a), bin(b)) #   二进制表示

print("二进制位与",a&b, bin(a&b))
print("左移运算a",a<<2,bin(a<<2))


# 逻辑运算符 and or not
'''
Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:

运算符	 逻辑表达式 	描述	     实例
and	    x and y	    布尔"与" -      如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
or	    x or y	    布尔"或" -      如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not	    not x	    布尔"非" -      如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
'''

# 成员运算符 判断成员在还是不=不在
'''
运算符       描述
in          如果在指定的序列中找到值，返回true 否则返回FALSE  
not in      如果在指定的序列中没有找到值，返回true
'''

# 运算符优先级

'''
以下表格列出了从最高到最低优先级的所有运算符：

运算符	        描述
**	        指数 (最高优先级)
~ + -	    按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	乘，除，取模和取整除
+ -	        加法减法
>> <<	    右移，左移运算符
&	        位 'AND'
^ |	        位运算符
<= < > >=	比较运算符
<> == !=	等于运算符
= %= /= //= -= += *= **=	赋值运算符
is is not	身份运算符
in not in	成员运算符
and or not	逻辑运算符'
'''



