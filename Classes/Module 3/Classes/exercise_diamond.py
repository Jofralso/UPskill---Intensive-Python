class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Name: {self.name}\nEmployee ID: {self.employee_id}")


class Teacher(Employee):
    def teach(self):
        print("Teaching students")


class Administrator(Employee):
    def manage(self):
        print("Managing administrative tasks")


class SupportStaff(Employee):
    def support(self):
        print("Providing support services")


class SchoolEmployee(Teacher, Administrator, SupportStaff):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")


employee = SchoolEmployee("John Doe", 12345, "Math Department")
employee.display_info()

employee.teach()
employee.manage()
employee.support()
