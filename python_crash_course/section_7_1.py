# -*- coding: utf-8 -*-

# input获取输入示例
message = input("告诉我一些内容，我读给你\n")
print(message)

# int()函数示例
age = input("告诉我你的年龄：\n")
age = int(age)
if age > 18:
    print("你已经成人了!")
else:
    print("你还未成人！")

# while循环
current_number = 0
while current_number < 15:
    current_number += 1

    if current_number == 9:
        break

    if current_number % 4 == 0:
        print("%d 是4的倍数" % current_number)
    else:
        continue
