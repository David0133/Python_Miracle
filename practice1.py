# 1. Swap the values of two variables without using a temporary variable.

# 2. Calculate the area of a rectangle given its length and width.

# def areaOfRectangle(length, width):
#     area = length * width
#     return area
#
#
# print("Find area of rectangle\n")
# length = float(input("Enter the length - \n"))
# width = float(input("Enter the width - \n"))
#
# result = areaOfRectangle(length, width)
# print("The area of rectangle is - ", result)


# 3. Concatenate two strings and print the result.

# firstname = input("Enter your first name - \n")
# lastname = input("Enter your last name - \n")
# # add method to add to strings
# result = firstname.__add__(lastname)
# result = result.upper()
# print(result)

# 4 Calculate the factorial of a given number.
# print("Calculating the factorial\n")
# value = int(input("Enter the number whose factorial you want - \n"))
#
#
# def factorial(value):
#     result = value
#     if value == 0 or value == 1:
#         return 1
#     while value > 1:
#         value = value -1
#         result = result*value
#
#     return result
#
#
# output = factorial(value)
# print(f"The factorial of the given number {value} is - ", output)


# 5. Calculate the sum of squares for a given range of numbers.
# print("Sum of squares for a given range")
# number = int(input("Enter the number upto which you want the sum of squares"))
# result = 0
# for i in range(1, number+1):
#     i = i ** 2
#     result = result + i
#
# print(f"The sum of square upto {number} is - ",result)

# 6. Count the number of vowels in a given string.

# vowels = ["a","e","i","o","u"]
# print("Counting the number if vowels in a given string - \n")
# user_input = input("Enter the word - \n")
# count = 0
# for i in user_input:
#     if vowels.__contains__(i):
#         count = count +1
#     else:
#         continue
# consonants = len(user_input) - count
# print("The number if vowels in a word is - ",count)
# print("The number of consonants in a word is - ",consonants)

# 7. Write a function to find the maximum of three numbers.
# print("The maximum of three numbers - ")
# maximum = 0
# for i in range(1,4):
#     value = float(input("Enter the first number - \n"))
#     if value > maximum :
#         maximum = value
#     else:
#         continue
# print("The highest value you have entered is - ", maximum)

# 8. Write a function to reverse a string.
# print("String reversing")
# word = input("Enter a word")
# ls = []
#
#
# def reverse(word):
#     for i in word:
#         ls.append(i)
#
#
# reverse(word)
# ls.reverse()
# result = ""
# # making string
# for i in ls:
#     result += i
#
# print("The word is reversed", result)

# 9. Perform basic operations on a list (append, remove, pop, etc.)

# ls = ["ram","shyam","calm","dam"]
# # Append
# ls.append("viram")
# # Remove
# ls.remove("calm")
# # Pop this will pop the element whose index you passed
# ls.pop(2)
# # Reverse
# ls.reverse()
# # count duplicates
# ls.count("ram")
# # clear will clear the list
# # ls.clear()
#
# print(ls)

# 10. Sort a list of numbers in ascending and descending order.
# ls = ["ram","shyam","calm","dam"]
# ls.sort(key=None,reverse=False)
# print("List in ascending order",ls)
# ls.sort(key=None,reverse=True)
# print("List in descending order",ls)

# 11. Create a new list with the squares of elements from an existing list using list comprehension.
# ls = [10,20,30,40]
# newList = []
# add = 0
# for x in ls:
#     add = x**2
#     newList.append(add)
#
# print("The new List is - ",newList)

# 12. Remove duplicates from a list.
# ls = [2,5,7,2,8,7,7]
# count = 0
# for i in ls:
#     count = ls.count(i)
#     if count == 1:
#         continue
#     else:
#         ls.remove(i)
# print(ls)

# 12 .Perform set union, intersection, and difference operations.
s = {1, 2, 3, 4, 5}
t = {1, 2, 6, 7}

# Union method make a new set and check the existing elements and the new elements
result = s.union(t)

# interaction method find's the common elements of two set and give a new set
interac = s.intersection(t)

# difference method is used to find out the different elements of two sets
# diff = s.difference(t)
#
# print("union method", result)
# print("interaction method", interac)
# print("Difference method", diff)
#
# # Check if one set is a subset of another
length1 = len(s)
length2 = len(t)
size = 0
if length1 > length2:
    size = length1
else:
    size = length2

count = 0
print()
