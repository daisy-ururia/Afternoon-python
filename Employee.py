class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def info(self):
        print(self.position, "is earning", self.salary)

employee1 = Employee("John", "CEO", 345000)
print(employee1.name, employee1.position, employee1.salary)
employee1.info()
employee2 = Employee("Jane", "Managing Director", 345000)
print(employee2.name, employee2.position, employee2.salary)
employee2.info()
employee3 = Employee("Joseph", "Secretary", 50000)
print(employee3.name, employee3.position, employee3.salary)
employee3.info()

