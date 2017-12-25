# -*- coding: utf-8 -*-

# 声明字典
dict1 = {'key1': 'value1', 'key2': 1}
print("字典示例：" + str(dict1))

# 添加键值对
dict1['key3'] = 'value3'
print("添加键值对后：" + str(dict1))

# 修改键对应的值
dict1['key1'] = 'new_value1'
print("修改键对应值后：" + str(dict1))

# 删除键值对
del dict1['key1']
print("删除键值对后：" + str(dict1))

# 遍历字典
for key, value in dict1.items():
    print("%s=%s" % (key, str(value)))
