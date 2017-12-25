# -*- coding: utf-8 -*-

cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print("我是宝马")
    else:
        print("我不是宝马")

# if语句
age = 19
if age > 18:
    print("你达到了选举年龄")
    print("你还没有注册选举？")

# if-else语句
age = 17
if age > 18:
    print("你达到了选举年龄")
    print("你还没有注册选举？")
else:
    print("你还未达到选举年龄")
    print("请你到18岁时再注册选举")
# if-elif-else语句
age = 12
if age < 4:
    price = 0
elif age < 10:
    price = 5
elif age < 64:
    price = 10
else:
    price = 6

print("价格是：" + str(price))
