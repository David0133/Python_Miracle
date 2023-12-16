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


print("\n")
print("\t\t\t\t\tWELCOME TO THE CALCULATOR\t\t\t\t\t\n")
# List to store the resultant output
ls = []
while True:

    print("\t\t\t\t\tPlease Choose one Option\n"
          "\t\t\t1. Addition\t\t\t\t""2. Subtraction\n"
          "\t\t\t3. Multiplication\t\t""4. Division\n"
          "\t\t\t5. Moduls\t\t\t\t""6. Percentage\n\n"
          "\t\t\t\t\t\t7. Exit\n")
    size = len(ls)
    if size > 0:
        print(f"\t\t\t\t\t\tYour Result is \n"
              f"\t\t\t\t\t\t\t{ls[0]}\n")
        ls.clear()

    while True:
        try:
            user_input = int(input("\t\t\t\t\t\tEnter Here\n\t\t\t\t\t\t\t"))
            print("\n")
            break
        except ValueError:
            print("\t\t\t\tInvalid input enter a valid input\n")

    if 0 < user_input <= 7:
        if user_input == 7:
            print("\t\t\t\t\tExited Successfully")
            break
        number1 = float(input("\t\t\t\t\tEnter the first number \n"
                              "\t\t\t\t\t\t\t"))
        if user_input != 6:
            number2 = float(input("\t\t\t\t\tEnter the second number \n"
                                  "\t\t\t\t\t\t\t"))
            print("\n")
    else:
        print("\t\t\t\t\tEnter a valid option\n")
        continue

    result = None
    if user_input == 1:
        result = add(number1,number2)
        ls.append(result)
    elif user_input == 2:
        result = sub(number1, number2)
        ls.append(result)
    elif user_input == 3:
        result = mul(number1, number2)
        ls.append(result)
    elif user_input == 4:
        while True:
            if number2 == 0:
                print("second number is invalid enter a valid number")
                number2 = float(input("Enter here - "))
            else:
                break
        result = div(number1, number2)
        ls.append(result)

    elif user_input == 5:
        result = mod(number1, number2)
        ls.append(result)
    elif user_input == 6:
        percentage = float(input("\t\t\tEnter the percentage you want to find - \n"
                                 "\t\t\t\t\t\t\t"))
        result = per(number1, percentage)
        ls.append(result)
    else:
        print("Enter a valid option")
