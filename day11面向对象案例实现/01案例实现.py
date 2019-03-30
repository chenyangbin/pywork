# 定义3个类,猫 ,狗, 人
# 狗: 姓名,年龄(默认1岁).   吃饭,玩儿,睡觉,看家
# 猫: 姓名.年龄(默认1岁),   吃法,玩儿,睡觉,捉老鼠
# 人: 姓名,年龄(默认1),     宠物: 吃饭,玩儿,睡觉, 养宠物,让宠物工作

class Dog:
    # 创建小狗实例,自动初始化
    def __init__(self,name,age = 1):
        self.name = name 
        self.age = age

    def eat(self):  #小狗吃
        print("名字是{},年龄{}岁的小狗在吃饭{}".format(self.name, self.age))

    def play(self):  #小狗玩儿方法
        print("名字是{},年龄{}岁的小狗在玩儿".format(self.name,self.age))    

    def sleep(self):  #小狗睡方法
        print("名字是{},年龄{}岁的小狗在睡觉".format(self.name,self.age))

    def __str__(self):
        



dog_hei = Dog("小黑", 12)
print(dog_hei.eat())

print(dog_hei.__dict__)

