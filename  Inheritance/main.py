class Employee:
    # name, age, salary
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print("Working")


class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def work(self):
        print(f"Managing the department: {self.department}")


emoployee = Employee("Jay", 25, "15k")
print(emoployee.work())
manager = Manager("King", 35, "25k", "HR")
print(manager.work())
