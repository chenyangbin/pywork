# 工程目录：c:\Users\bin\OneDrive\share\pywork\day02\05.1字符串-处理函数.py
# 创建日期: 2019.02.13
# 工程目标： 常用字符串 处理 函数的使用练习
# 创建作者：binyang
# -*- coding:utf-8 -*-

str1 = 'this is a test string'


# 01 capitalize()   将字符串的第一个字符转换为大写
print("capitallize 首字母大写", str.capitalize(str1))


# 02center()   剧中填充 center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
'''
str.center(width[, fillchar])
width -- 字符串的总宽度。
fillchar -- 填充字符。
'''
print("center 居中填充", str1.center(40, "*"))
print("center 居中填充，默认空格", str1.center(40))    # fillchar默认是空格


# 03bytes.decode() 字节包解码为字符串的函数
'''
bytes.decode(encoding="utf-8", errors="strict")
Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，
这个 bytes 对象可以由 str.encode() 来编码返回。
decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。

参数：
encoding -- 要使用的编码，如"UTF-8"

errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。
其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。

返回值：
该方法返回解码后的字符串
'''
# 字符串的编码和解码示例
print("-----字符串的编码，字节包解码-----")
str2 = "编码解码测试"
str_utf8 = str2.encode('utf-8')
str_gbk = str2.encode('GBK')
str_utf8_de = str_utf8.decode('utf-8')
str_gbk_de = str_gbk.decode('gbk')

print("原始str:",str2)
print("strutf-编码结果： ", str_utf8)
print("strgbk编码结果：", str_gbk)
print("str_utf8_de解码结果：", str_utf8_de)
print("str_gbk_de解码结果：", str_utf8_de)


# 06 endswith()  方法	endswith(suffix, beg=0, end=len(string))
'''
用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。

endswith()方法语法：
str.endswith(suffix[, start[, end]])

参数
suffix -- 该参数可以是一个字符串或者是一个元素。
start -- 字符串中的开始位置。
end -- 字符中结束位置。

返回值
如果字符串含有指定的后缀返回True，否则返回False
'''
# 判断某段字符串是否以指定后缀结尾
print("-----判断某段字符串是否以指定后缀结尾-----")
str3 = "你好我是斌飏"
print(str3.endswith("斌", 0, 5))
print(str3.endswith("飏", 0, 6))
print(str3.endswith("飏"))  # 默认是从头到尾

# 09 find()方法 str.find(str, beg=0, end=len(string))
'''
find() 方法检测字符串中是否包含子字符串 str ，
如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。

find()方法语法：
str.find(str, beg=0, end=len(string))

参数
str -- 指定检索的字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。

返回值
如果包含子字符串返回开始的索引值，否则返回-1
'''
# find 指定段落查找字符串。。
# str3 你好我是斌飏
print("------find查找字符串-----")
print(str3.find("我是"))
print(str3.find("步"))
print(str3.find("是", 1, 4))

# 10