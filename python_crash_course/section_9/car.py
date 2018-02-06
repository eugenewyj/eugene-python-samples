# -*- coding: utf-8 -*-


class Car:
    """一次模拟汽车的尝试"""

    def __init__(self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        log_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return log_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读书设置为指定值"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """
        将里程表读数增加指定值。
        :param miles:
        :return:
        """
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

