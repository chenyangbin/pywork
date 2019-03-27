# 工程目录：c:\Users\bin\OneDrive\share\pywork\day01\python的bites和str的区别.py
# 创建日期: 2019.02.11
# 工程目标：bite文件（二进制文件），包括mp3，mp4。   str文件（unicode）包括txt文本
# 创建作者：binyang
# -*- coding:utf-8 -*-

# 字符串str 和字节包文件 在python3中有明显的区分，不可以拼接str 和 bites 文件
# 字符串string可以编码成字节包bytes，字节包也可以解码成字符串 其过程要有解码编码过程

#

code = "my code 你好"

print("origin code:",code)

en_code = code.encode(encoding="utf-8")

print("en_code: ",en_code)

de_code = en_code.decode(encoding="utf-8")

print("de_code",de_code)
