class SoftwareEngineer:
    
    alias = 'Keyboard Warrior'
    
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
        
se1 = SoftwareEngineer("John", 30, "Senior", 100000)
print(se1.name)
se2 = SoftwareEngineer("Mary", 25, "Junior", 50000)
print(se2.name, se2.age, se2.level, se2.salary)
print(se1.alias)
print(SoftwareEngineer.alias)

#class (blueprint)
#object (instance)
#instance attributes: defined by __init__
#class attributes: defined by class        