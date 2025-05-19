

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         #public variable
        self._salary = salary    #protected variable
        self.__ssn = ssn         #private variable


Noor_ul = Employee("Noor ul huda", 100000, 123456789)    

print(Noor_ul.name)
print(Noor_ul._salary)
# print(Noor_ul.__ssn)    private variable can't be accessed

print(Noor_ul._Employee__ssn)
        