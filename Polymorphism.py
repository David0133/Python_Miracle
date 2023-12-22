"""
Compile time polymorphism is achieved by the use of method overloading
In python it is not following the traditional way for method overloading
if you want to overload the method you have to implement the login according to your parameter
"""


class Claculator:
    def add(self,number1,number2,number3=None,number4=None):
        if number3 is not None and number4 is None:
            print(number1+number2+number3)
        elif number4 is not None and number3 is not None:
            print(number1+number2+number3)
        else:
            print(number1+number2)

calculator = Claculator()
calculator.add(2,3)