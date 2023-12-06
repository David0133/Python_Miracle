# Operator
# Arithmetic operator
num1 = 4
print(num1 + 10)
print(num1 - 2)
print(num1 * 2)
print(num1 / 2)
print(num1 // 2)
print(num1 ** 2)
print(num1 % 2)

# Comparison operator
num2 = 10
print(num1 > num2)

# Logical operator
# wap for creating admission system there check if the student is male and hos age is more then 19 allow for the admission

age_of_student = int(input("Enter your age : "))
gender = input("Enter your gender ")
gender.lower()

if age_of_student > 19 and gender == "male":
    print("You are allowed for the admission")
else:
    print("You are not allowed for the admission")

value = True
print(not(value))

student_list = ["Aakash", "Vikash", "Mahendra", "David", "Faizan", "Narendra"]
student_name = "Aakash"
if student_name in student_list :
    print("Present")
else:
    print("Not present")