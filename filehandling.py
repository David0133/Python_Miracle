# file = open("new.txt","w")
# file.write("Hey! this is file handling")
# file.close()
# file = open("new.txt","r")
# read = file.read()
# print(read)

# with open("new.txt","r") as file :
#     content = file.read()
#     print(content)


# write a program to create a dynamic file system where perform all the operation of file using user input

while True:
    container = ""
    print("Enter which operation you want to perform\n"
          "1.Read\n"
          "2.Write\n"
          "3.Exit")
    while True:
        try:
            option = int(input())
            break
        except ValueError as e:
            print("Not a valid input")

    if option == 1:
        print("1.Read-Line\n"
              "2.Read-Line's\n")
        while True:
            try:
                option = int(input())
                break
            except ValueError as e:
                print("Not a valid input")

        if option == 1:
            while True:
                try:
                    num_char = int(input("Enter the number of character you want to print from a line"))
                    break
                except ValueError:
                    print("Please! enter a valid input\n")

            with open("new.txt", "r") as file:
                container = file.readline(num_char)
                print(container)
                break
        elif option == 2:
            with open("new.txt", "r") as file:
                container = file.readlines(2)
                print(container)

        elif option == None:
            file = open("new.txt", "r")
            container = file.read()
            print(container)
            break
    elif option == 2:
        write_option = int(input("Enter your choice of operation\n"
                                 "1.Write\n"
                                 "2.Write-Line's\n"))
        if write_option == 1:
            with open("new.txt", "a") as file:
                container = file.write(input())
                break
        elif write_option == 2:
            with open("new.txt", "a") as file:
                container = file.writelines(input())
                break
    elif option == 3:
        break