# -*- coding: utf-8 -*-

age = 23
# message = "Happy " + age + "rd Birthday!"  # 此语句会报错，正确应该使用str
message = "Happy " + str(age) + "rd Birthday!"
print(message)