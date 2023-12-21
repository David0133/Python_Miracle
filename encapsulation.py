class Employee:
    def __int__(self,emp_id,emp_name,emp_designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_designation = emp_designation

    def display(self):
        print(f"{self.emp_id} {self.emp_name} {self.emp_designation}")

class Developer(Employee):
    def __int__(self,emp_id,emp_name,emp_designation,backend_id,developer_id):
        super().__int__(emp_id=emp_id,emp_name=emp_name,emp_designation=emp_designation)
        self.is_backend_id = backend_id
        self.developer_id = developer_id

    def display(self):
        print(f"{self.emp_id,self.emp_name,self.emp_designation,self.is_backend_id,self.developer_id}")


developer = Developer()
developer.__int__("205","David","Developer",True,"600")
developer.display()


# employee = Employee()
# employee.__int__("205","David","Developer")
# employee.display()

