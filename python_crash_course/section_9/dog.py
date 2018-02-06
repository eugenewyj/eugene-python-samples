# -*- coding: utf-8 -*-


class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """构造函数：初始化属性name, age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令式蹲下"""
        print(self.name.title() + " 正在蹲下...")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " 打滚！")


my_dog = Dog("旺财", 6)

print("我的狗名字是" + my_dog.name.title() + "。")
print("我的狗年龄是" + str(my_dog.age) + "。")