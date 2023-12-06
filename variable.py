# variable
# Numerica Data type
# var = 23
# print(var)
# float_value = 1.8
# print(float_value)

# Sequence
# str_value = "This is a string"
# print(str_value)
#
# list_value = [1, 2, 3, 5, 7, 5, 6]
# print(list_value[2])
#
fruits = ["apple", "Banana", "Grapes", "Banana", "orange", "Mango"]
# updated_fruits = fruits.append("lichi")
# print(fruits)
#
# fruits.sort()
# print(fruits)

# different methods in list

# fruits_count = fruits.count("Banana")
# print("The count method will give you the number of times an element found in the list : - ", fruits_count)
# fruits.insert(1, "Pineapple")
# print("insert method insert the element on the index we gave on it - ", fruits)
# fruits.reverse()
# print("reverse method reverse the list - ",fruits)
# fruits2 = fruits.copy()
# print("copy function copies the list -", fruits2)
# fruits.extend('man')
# print("extend method will extend the already present list upto the give word length", fruits)
# fruit_index = fruits.index("Grapes")
# print("The index of the given fruit is - ", fruit_index)
# fruits.remove("Pineapple")
# print("The fruit is removed - ", fruits)
# is_fruit_available = fruits.__contains__("orange")
# print("contains method check the element is available or not gave you the boolean value - ", is_fruit_available)
# list_size = fruits.__sizeof__()
# print("The size of list in memory in bytes - ", list_size)
# fruits.clear()
# print(fruits)
# Write a program to perform all the function that are available in list

tuple_value = (1, 2, 3, 4, 2, 2)
# var = tuple_value.count()
# print(var)
tuple_index = tuple_value.index(3)
print("The index of the given element in tuple is  - ", tuple_index)
tuple_count = tuple_value.count(2)
print("Number of time an element occurred in a tuple - ", tuple_count)

is_authenticated = bool(int(input("Enter 0 for false and 1 for true")))

print(type(is_authenticated))

if is_authenticated:
    print(is_authenticated)
    print("You are allowed")
else:
    print("Not allowed")

my_set = {1, 5, 2, 6, 2, 5}

# Dict
dict_type = {
    "Name": "David",
    "address": "Bhopal",
    "Mob No.": "8319227993"
}
print(dict_type.values())
dict_type.update({"course" : "Full stack"})
dict_item = dict_type.items()
print(dict_item)
dict_keys = dict_type.keys()
print(dict_keys)
