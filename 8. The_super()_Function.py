

class Person:                    # Parent class
    def __init__(self, name):
        self.name = name


class Teacher(Person):           # Child class
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


teacher1 = Teacher("Noor ul huda", "Maths")

print(teacher1.name)
print(teacher1.subject)

        