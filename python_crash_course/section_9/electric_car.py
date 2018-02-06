# -*- coding: utf-8 -*-


from car import Car


class ElectricCar(Car):
    """电动汽车独特之处"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_descriptive_name(self):
        """打印简洁的描述信息"""
        return str(self.year) + ' ' + self.make + ' ' + self.model + ' ' + str(self.battery_size)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
