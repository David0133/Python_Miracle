# Creating a dynamic calculator
"""
Features
addition
subtraction
multiplication
division
moduls
percentage
"""


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def mod(num1, num2):
    return num1 % num2


def per(num, percentage):
    return num * (percentage / 100)


print("WELCOME TO THE CALCULATOR")

while True:
    print("Please Choose one Option\n"
          "1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5. Moduls\n"
          "6. Percentage\n"
          "7. Exit")
    user_input = int(input())
    if user_input == 7:
        break
    number1 = float(input("Enter the first number"))
    number2 = float(input("Enter the second number"))
    result = None
    if user_input == 1:
        result = add(number1, number2)
        print(f"The result of your addition is {result}")
    elif user_input == 2:
        result = sub(number1, number2)
        print(f"The result of your Subtraction is {result}")
    elif user_input == 3:
        result = mul(number1, number2)
        print(f"The result of your Multiplication is {result}")
    elif user_input == 4:
        while True:
            if number2 == 0:
                print("Enter a valid number")
                number2 = float(input())
            else:
                break
        result = div(number1, number2)
        print(f"The result of your Division is {result}")
    elif user_input == 5:
        result = mod(number1, number2)
        print(f"The result of your Moduls is {result}")
    elif user_input == 6:
        percentage = float(input("Enter the percentage"))
        result = per(number1, percentage)
        print(f"The result of your Percentage is {result}")
    else:
        print("Enter a valid choice")
