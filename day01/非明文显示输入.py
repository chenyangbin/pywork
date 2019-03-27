# 工程目录：c:\Users\bin\OneDrive\share\pywork\day01\非明文显示输入.py
# 创建日期: 2019.02.10
# 工程目标：非明文输入  getpass
# 创建作者：binyang
# -*- coding:utf-8 -*-\

import getpass

username = input("username: ")
password = input("password: ")

passwordmi = getpass.getpass("passwordmi: ")   # 使用getpass在输入内容的时候 不会显示输入状态


print(username,password,passwordmi)