class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"The total marks {self.marks} obtainted by student {self.name}")

student1 = Student("Noor ul huda" , 85)

student1.display()
