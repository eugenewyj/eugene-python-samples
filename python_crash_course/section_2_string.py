# -*- coding: utf-8 -*-

name = "eugene wang"
print(name.title())
print(name.upper())
print(name.lower())

# 连接字符串
first_name = "eugene"
last_name = "wang"
full_name = first_name + " " + last_name
print(first_name)
print(last_name)
print(full_name)

# 去除字符串前后空格
str_with_space = ' 包含前后空格字符串  '
print("|" + str_with_space + "|")
print("|" + str_with_space.rstrip() + "|")
print("|" + str_with_space.lstrip() + "|")
print("|" + str_with_space.strip() + "|")
