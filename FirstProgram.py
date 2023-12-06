#write a program from give a message "Hello World"

#print("Hello world") # print is a function which we can use to display statement

#write a program to take a message and print with your name using variable

greeting_message = "Good morning"
name = "David"

#print(f"Hello {name} {greeting_message},How are you?")  #To insert a variable inside the string we have use fstring and {}

company_name = "Miracle Infoserv"
address = "Zone-2 mp nagar"
subject = "Application for leave"
main_content = (f"My self {name} and i am one of the student of your institute in Full stack course\n"
                f"today i am not feeling well so i am not able to attend today's class so please accept\nthis application"
                f" and give me 1 day of leave.")
end = "Thankyou"
date = "04-12-2023"
print("\t\t\t\t\tApplication\t\t\t")
print("")
print("To,")
print("The,")
print("Head of department")
print(company_name)
print(address)
print(f"Date {date}")
print("")
print(f"Subject : {subject}")
print("")
print(f"Dear sir/madam, \n{main_content}")
print("")
print(f"{end}\n"
      f"your obedient student\n"
      f"{name}")

first_num = 23
second_num = 25
print(first_num+second_num)