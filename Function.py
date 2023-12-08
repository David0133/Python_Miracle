# def add(a, b):
#     c = a + b
#     print("The addition of two number is  - ", c)
#
#
# add(5, 2)
def greeting_display(name, greet):
    # print(f"Hello {name} {greet}")
    print("Hello", name, greet)


name = input("Enter your name : ")
greeatings = input("Enter your message like Good morning / Good after noon / Good Evening /Good Night ")
greeting_display(name, greeatings)
