# -*- coding: utf-8 -*-

# 循环列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 元组
tuples = (100, 200, 300)
for each in tuples:
    print(each)

# list,range函数构造数字列表
numbers = list(range(1, 6))
print(numbers)

print(list(range(2, 11, 2)))

squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

# 列表计算函数
digits = list(range(0, 11))
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)
