# How to use switch statement

# Loops in python
# loop is used to perform the iteration on the same code with given condition


# WAP to print all the month  in list in a order of insertion


ls = []
count = 0
while count < 12:
    month = input("Enter the first month ")
    month.lower()
    ls.append(month)
    count = count + 1

for i in ls:

    index = ls.index(i)
    if index % 2 == 0 and i != "feb":
        print(f"The month {i} has 31 days in a month")
    elif index % 2 != 0 and i != "feb":
        print(f"The month {i} has 30 days in a month")
    elif i == "feb":
        print(f"The month {i} has 28 days in a month")
