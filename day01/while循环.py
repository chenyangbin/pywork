# 工程目录：c:\Users\bin\OneDrive\share\pywork\day01\while循环.py
# 创建日期: 2019.02.10
# 工程目标：while循环
# 创建作者：binyang
# -*- coding:utf-8 -*-

age = 23
count = 0

"""

while True:

    guess_age = int(input("guess lala :"))

    count+=1

    if guess_age == age:
        print("right")
        break

    elif guess_age > age:
        print("guess smaller please ")

    elif guess_age < age:
        print("guess bigger please ")

    if count > 3:
        print("you loss ")
        break
        
    """
    
while count <3 :
    
    guess_age = int(input("guess lala :"))

    count+=1

    if guess_age == age:
        print("right")
        break
    elif guess_age > age:
        print("guess smaller please ")

    elif guess_age < age:
        print("guess bigger please ")
    else:
        print("you loss")

    if count == 3:
        countine_flag = input("keep going..?")
        if countine_flag != "n":
            count =0
            
