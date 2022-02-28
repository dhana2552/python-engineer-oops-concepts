class SoftwareEngineer:
    
    #class attribute
    alias = 'Keyboard Warrior'
    
    def __init__(self, name, age, level, salary):
        #instance attribute
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    
    #instance method
    def code(self):
        print(f"{self.name} is coding...")
        
    def code_in_language(self, language):
        print(f"{self.name} is coding in {language}")
        
    #dunder method
    def __str__(self):
        information = f'{self.name} is {self.age} years old, {self.level} and earns {self.salary}'
        return information
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    #if the attribute is not expected to tie with the class attribute, use @staticmethod
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 10000
        return 15000
    

        
se1 = SoftwareEngineer("John", 30, "Senior", 100000)
se1.code()
se1.code_in_language("Python")
print(se1)
se2 = SoftwareEngineer("Mary", 25, "Junior", 50000)
print(se2)
se3 = SoftwareEngineer("Mary", 25, "Junior", 50000)
print(se2 == se3)

print(SoftwareEngineer.entry_salary(25))
print(se1.entry_salary(25))

#Recap
#instance method(self)
#can take arguments and can return values
#special dunder methods (__str__, __eq__)
#staticmethod