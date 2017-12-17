# -*- coding: utf-8 -*-

list_samples = ['元素1', '元素2', '元素3', '元素4']
print(list_samples)

# 获取列表指定元素
print(list_samples[0].title())
print(list_samples[-1].title())

# 修改元素
list_samples[0] = '修改后的元素1'
print(list_samples)

# 末尾添加元素
list_samples.append("末尾添加元素")
print(list_samples)

# 插入元素
list_samples.insert(0, "新插入元素")
print(list_samples)

# 删除元素
del list_samples[0]
print(list_samples)

# pop删除
last_item = list_samples.pop()
print(list_samples)
print(last_item)
pop_item = list_samples.pop(0)
print(list_samples)
print(last_item)

# remove
list_samples.remove('元素2')
print(list_samples)

# 排序
list_samples.sort(reverse=True)
print(list_samples)
list_samples.sort(reverse=False)
print(list_samples)

print(sorted(list_samples, reverse=True))
print(list_samples)

# 反向排序
list_samples.reverse()
print(list_samples)
