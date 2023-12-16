class Employee:
    # name = "David"
    # age = "23"
    # address = "Bhopal"
    # designation = "FSD"
    # organization = "Deloitte"

    # Constructor
    nn = 20

    def __init__(self):
        print("This is default constructor")

    def __init__(self, name, age, address, designation, organization):
        self.name = name
        self.age = age
        self.address = address
        self.designation = designation
        self.organization = organization

    def display_data(self):
        print(self.name, self.age, self.address, self.designation, self.organization)


obj = Employee("David", 23, "Home", "FSD", "Deloitte")
obj.display_data()

obj1 = Employee()
print(obj1)
