# 工程目录：c:\Users\bin\OneDrive\share\pywork\day01\login.py
# 创建日期: 2019.02.11
# 工程目标：login.第三杠模块 自定义
# 创建作者：binyang
# -*- coding:utf-8 -*-


#调用第三方模块 自定义模块，要把该模块放在sitepacge的包文件夹中
# 或者使用sys模块更改环境变量，引入该模块

log_name = bin
log_password = 23

name = input("请输入用户名：")

password =input("请输入登陆密码：")

info = '''

----------登陆信息------

用户名：{0}

密码：{1}

'''.format(name,password)

if name == log_name and password == log_password:
    print("right")
    print(info)

else:
    print("请重新输入")



