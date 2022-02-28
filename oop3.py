#inherit, extend, override
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    #instance method - for inheritance
    def work(self):
        print(f'{self.name} is working...')

class SoftwareEngineer(Employee):
    
    #override __init__
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level
    
    #override work()
    def work(self):
        print(f'{self.name} is coding...')
        
    def debug(self):
        print(f'{self.name} is debugging...')

class Designer(Employee):
    
    def work(self):
        print(f'{self.name} is designing...')
    
    def draw(self):
        print(f'{self.name} is drawing...')


se = SoftwareEngineer("John", 30, 100000, "Senior")
#se.work()


d = Designer("Mary", 25, 50000)
#d.work()

#Polymorphism
employees = [SoftwareEngineer("John", 30, 100000, "Senior"),
             SoftwareEngineer("Mary", 25, 50000, "Junior"),
             Designer("Jack", 35, 200000)]

def motivate_employee(employees):
    for employee in employees:
        employee.work() #takes specific implementation of the child class - Polymorphism
        
motivate_employee(employees)


#Recap
#Inheritance: ChildClass(ParentClass)
#inherit, extend, override
#super().__init__(name, age, salary)
#polymorphism
