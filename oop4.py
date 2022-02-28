#Encapsulation

class SoftwareEngineer:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None #private attribute
        self.__num_of_bugs_resolved = 0 #protected attribute
        
    
    def code(self):
        self.__num_of_bugs_resolved += 1
        
    #getter
    def get_salary(self):
        return self._salary
    
    #setter
    def set_salary(self, base_value):
        #enforce constraint
        self._salary = self._calculate_salary(base_value)
        
    #private method
    def _calculate_salary(self, base_value):
        if self.__num_of_bugs_resolved < 10:
            return base_value
        if self.__num_of_bugs_resolved < 100:
            return base_value * 2
        return base_value * 3
        

se = SoftwareEngineer("John", 30)


for i in range(70):
    se.code()

se.set_salary(800)
print(se.get_salary())

#Abstraction - hiding details and only high level details are exposed. _calculate_salary is an example here