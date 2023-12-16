# 1. Write a program that takes a user's name and age and prints a message with this information

# user_name = input("Enter your good name")
# age = int(input("Enter your age : "))
#
# print(f"Hii {user_name} your age is {age} ")


# 2. Create a simple calculator that can perform addition,Subtraction,multiplication,and division
# def addition(num1, num2):
#     return num1 + num2
#
#
# def subtraction(num1, num2):
#     return num1 - num2
#
#
# def multiplication(num1, num2):
#     return num1 * num2
#
#
# def division(num1, num2):
#     return num1 / num2
#
#
# result = 0
# number1 = int(input("Enter your first number\n "))
# number2 = int(input("Enter your second value\n "))
# operation = input("Enter what you want to do like +,-,*,/ \n")
# if operation == "+":
#     result = addition(number1, number2)
#     print("The addition of the given number is : - ", result)
# elif operation == "-":
#     result = subtraction(number1, number2)
#     print("The subtraction of the given number is : - ", result)
# elif operation == "*":
#     result = multiplication(number1, number2)
#     print("The multiplication of the given number is : - ", result)
# elif operation == "/":
#     result = division(number1, number2)
#     print("The division of the given number is : - ", result)
# else:
#     print("Wrong selection of operation enter valid operation")

# 3 Random Password

# user_input = list(input("Enter your some character and special symbol to generate password "))
# random.shuffle(user_input)
# password = ""
# for i in user_input:
#     password += i
# print("Your randomly generated Password is ", password)

# 4. Fahrenheit to celsius

# def fahr2celsius(value):
#     c = (value - 32) * 5 / 9
#     return c
#
#
# value_in_fahrenheit = int(input("Enter the value in fahrenheit - "))
# result = int(fahr2celsius(value_in_fahrenheit))
# print("The result of fahrenheit to celsius is - ", result, "C")

# 5. create a basic to-do list program that allows users to add delete, and view tasks.

# to_do_bucket = {}
# count = 0
# while True:
#
#     task = input("Enter the task for add type a, for remove r, for view v and x for exit")
#     task.lower()
#     if task == "a":
#         key = input("Enter the key ")
#         value = input("Enter the value ")
#         to_do_bucket = {key :value}
#         print("The item is added successfully ")
#
#     elif task == "r":
#         key = input("Enter the key ")
#         if to_do_bucket.__contains__(key):
#             to_do_bucket.pop(key)
#             print("The item is removed successfully ")
#
#         else:
#             print("Entered key not found ")
#     elif task == "v":
#         key = input("Enter the key ")
#         print(to_do_bucket.get(key))
#     elif task == "x":
#         break
# print(to_do_bucket)


# 6. Palindrome

# def palindrome(name, first, last):
#     length = name.__len__()
#     mid = int((length-1)/2)
#     # print(mid)
#
#     if length < 1:
#         return print("Invalid")
#     if length == 1:
#         return print("palindrome")
#     for i in name:
#         if name[first] == name[last] and first!=mid:
#             first = first + 1
#             last = last - 1
#         elif first == mid and name[first] == name[last]:
#             return print("Palindrome")
#         else:
#             return print("Not a palindrome")
#
#
# palin_drome = list(input("Enter the word - "))
# first_index = 0
# last_index = palin_drome.__len__() - 1
# palindrome(palin_drome, first_index, last_index)

# 7. ATM simulation

# balance = 0
# print("Welcome to Miracle ATM ")
# while True:
#     print("Choose option : Balance inquery - B Withdraw - W ADD - A  Exit - X")
#     task = input(" ")
#     task.lower()
#     if task == "a":
#         amount = int(input("Enter the amount "))
#         balance = balance + amount
#     elif task == "w":
#         amount = int(input("Enter the amount you want to withdraw"))
#         balance = balance - amount
#
#     elif task == "b":
#         print("Your current balance in the account is - ", balance)
#     elif task == "x":
#         break

# 8. multiplication table
# table_of = int(input("Enter whose table you want to print : "))
# for i in range(1, 11):
#     print(f"{table_of} x {i} =", table_of * i)


# 9 Number occurrence of a word

# ls3 = ["mango", "guava", "orange", "apple", "grapes", "grapes", "apple", "apple"]
# occurrence = input("Enter which fruit occurrence you want option's are\n"
#                    "mango,guava,orange,apple,grapes\n ")
# fruit_name = occurrence.lower()
# fruit_count = ls3.count(fruit_name)
# print(f"The occurrence of the give fruit {occurrence} is {fruit_count} ")


# 10 Write a program that checks if a given number is a prime number.


# user_input = int(input("Enter a number to check : "))
# if user_input == 1 or user_input == 2 or user_input == 3:
#     print(f"The given value {user_input} is a prime number : ")
# elif user_input % 2 == 0 or user_input % 3 == 0:
#     print(f"The given value {user_input} is not a prime number : ")
# else:
#     print(f"The given value {user_input} is a prime number : ")


# 11. Implement a basic text-based game (e.g., a quiz or a simple guessing game).

# print("Welcome to the game of guessing character's : ")
# to_find = "o"
#
#
# count = 3
# for i in range(1, 4):
#     ch_input = input("Enter your guessing character : ")
#     ch_input.lower()
#     if i <= count and ch_input == to_find:
#         print("WOW! Your guess is right ")
#         break
#     elif i == count and ch_input != to_find:
#         print("Ohh no you can't guess right Better luck next Time ")
#         break
#     else:
#         left = count-i
#         print(f"Remaining chance {left} ")


# 12. Create a program that reads data from a text file and prints it in reverse order


# file_object = open("temp.txt", "r")
# rev = str(file_object.read())
# ls = list(rev)
# counter = 0
# ls.reverse()
# st = str(ls)
# print(st)


# 13 Guess the number
# def guess_the_number(chance):
#     random_num = int(random.random() * 100)
#     while chance < 2:
#         user_guess = int(input("Enter your guessing number between 0 to 100 Only positive number allow : "))
#         if random_num == user_guess:
#           return print("Wow you guess it right ")
#         else:
#             chance += 1
#             print(f"You have only {2 - chance}")
#     return print("Better luck next time ")
#
#
# chance = 0
# print("Welcome to the guess game you have to guess the number under 2 chance \n\n")
# guess_the_number(chance)

