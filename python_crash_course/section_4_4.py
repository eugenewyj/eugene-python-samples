# -*- coding: utf-8 -*-

# 示例列表
list_samples = ['a', 'b', 'c', 'd', 'e']

# 根据列表生成切片
slice1 = list_samples[1:4]
print(slice1)   # ['b', 'c', 'd']

slice2 = list_samples[:4]  # ['a', 'b', 'c', 'd']
print(slice2)

slice3 = list_samples[-3:]  # ['c', 'd', 'e']
print(slice3)

# 循环切片
for each in list_samples[1:4]:
    print(each.title())

# 通过切片方式复制列表
slice4 = list_samples[:]  # ['c', 'd', 'e']
print(slice4)

# 切片复制与直接赋值区别
list_samples2 = list_samples
list_samples3 = list_samples[:]
list_samples2.append('g')
print("list_sample:" + list_samples.__str__())
print("list_sample2:" + list_samples2.__str__())

list_samples3.append('h')
print("list_sample:" + list_samples.__str__())
print("list_sample3:" + list_samples3.__str__())

