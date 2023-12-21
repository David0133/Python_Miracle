# Create a base class Person with attributes name and age.
# Derive a subclass Employee from Person with an additional attribute employeeId.
# Implement constructors for both classes and display the details of an employee.
# class Person:
#     # name = ""
#     # age = 0
#
#     # parameterized constructor
#     def __init__(self, f, s):
#         self.name = f
#         self.age = s
#
#
# class Employee(Person):
#     employeeId = 0
#
#     def __int__(self, i):
#         self.employeeId = i
#
#     def display(self):
#         print(self.name,self.age,self.employeeId)
#
#
# # creating object of the class
# # this will invoke parameterized constructor
# # obj1 = Person("David", 23)
# # obj2 = Employee(self,233)
# # print(obj2.employeeId)
# # obj2.display()
#
# obj = Employee(f=input(),s=int(input()))
# # obj.__init__(f="adadad",s=12)
# obj.__int__(12)
# obj.display()

"""Create a base class Shape with methods area and display.
 Derive two subclasses Circle and Rectangle from Shape.
 Override the area method in each subclass and demonstrate polymorphism.
"""

# class Shape:
#     length = 0
#     width = 0
#     radius = 0
#
#     def __int__(self, length, width, radius):
#         self.length = length
#         self.width = width
#         self.radius = radius
#
#     def area(self):
#         print("")
#
#     def display(self):
#         print("The length, Width and Radius is - ",self.length,self.width,self.radius)
#
#
# class Circle(Shape):
#     def __int__(self,r):
#         self.radius = r
#
#     def area(self):
#         result = (22 / 7) * self.radius ** 2
#         return result
#
#     def display(self):
#         print("The area of circle is ", self.area())
#
#
# class Rectangle(Shape):
#     def __int__(self, l, w):
#         self.length = l
#         self.width = w
#
#     def area(self):
#         result = self.length * self.width
#         return result
#
#     def display(self):
#         print("The area of rectangle is - ", self.area())
#
# # This is just for testing
# # firstobj = Shape()
# # firstobj.__int__(20,30,40)
# # firstobj.display()
#
# # Circle object
# obj = Circle()
# obj.__int__(20)
# obj.display()
#
# # Rectangle object
# obj1 = Rectangle()
# obj1.__int__(15, 20)
# obj1.display()


"""
Create a base class Animal with a method makeSound.
Derive two subclasses Dog and Cat from Animal.
Override the makeSound method to make each animal sound differently.
Create instances of both subclasses and call their makeSound methods
"""

# class Animal:
#     sound = ""
#     def __int__(self,sound):
#         self.sound = sound
#
#     def makeSound(self):
#         print("No sound")
#
# class Dog(Animal):
#     def makeSound(self):
#         print("Dog make the sound - ",self.sound)
#
# class Cat(Animal):
#     def makeSound(self):
#         print("Cat makes the sound - ",self.sound)
#
#
# dog = Dog()
# dog.__int__("BHAW BHAW")
# dog.makeSound()
#
# cat = Cat()
# cat.__int__("MEWW")
# cat.makeSound()

"""
Create a base class Vehicle with attributes model and year. 
Derive two subclasses Car and Motorcycle from Vehicle. 
Implement a method in each subclass to display information about the vehicle.
"""

# class Vehicle:
#     model = 0
#     year = 0
#     def __int__(self,m,y):
#         self.model = m
#         self.year = y
#
#     def vehicleInfo(self):
#         print(f"The vehicle model is {self.model} and year is {self.year}")
#
# class Car(Vehicle):
#     def vehicleInfo(self):
#         print(f"The car with the model number {self.model} is of year {self.year}")
#
# class Motorcycle(Vehicle):
#     def vehicleInfo(self):
#         print(f"The Motorcycle with the model number {self.model} is of year {self.year}")
#
#
# car = Car()
# car.__int__(256,2020)
# car.vehicleInfo()
#
# bike = Motorcycle()
# bike.__int__(1223,2022)
# bike.vehicleInfo()

"""
Create a base class Person with attributes name and address. 
Derive two subclasses Student and Teacher from Person. 
Add attributes specific to each subclass, such as grade for Student and subject for Teacher. 
Display the details of a student and a teacher.
"""


class Person:
    name = ""
    address = ""

    def __int__(self, n, a):
        self.name = n
        self.address = a


class Student(Person):
    grade = ""

    def __int__(self, g, n, a):
        self.name = n
        self.address = a
        self.grade = g

    def studentDetail(self):
        print(f"The Student name {self.name} got grade's {self.grade} and address {self.address}")


class Teacher(Person):
    subject = ""

    def __int__(self, s, n, a):
        self.name = n
        self.address = a
        self.subject = s

    def teacherDetails(self):
        print(f"Teacher name {self.name} is teaching the subject {self.subject} and address {self.address}")


student = Student()
student.__int__("A", "David", "Bhopal")
student.studentDetail()

teacher = Teacher()
teacher.__int__("English", "RK", "Bhopal")
teacher.teacherDetails()
