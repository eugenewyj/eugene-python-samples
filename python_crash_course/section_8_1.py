# -*- coding: utf-8 -*-


def func1(param1, param2='value2'):
    """函数注释样例"""
    print("param1=%s,param2=%s" % (param1, param2))
    return param1


print(func1("aa", "bb"))
print(func1("cc"))
print(func1(param2="ttt", param1="ff"))


def func2(*params):
    """打印所有参数"""
    for param in params:
        print("param=%s" % str(param))


print(func2(1, "a", 2))
print(func2("a", "b"))
print(func2(1, 2))
