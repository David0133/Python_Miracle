"""
Abstract class and method
A method to be abstract if it's class is abstract

"""

from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def demo(self):
        pass

    def demo(self, name):
        print("check")


class info(Car):
    def demo(self):
        print("Inherited")


# class info(Car)

obj = info()
obj1 = Car()
obj1.demo("David")
obj.demo()
