class Car:
    def __init__(self, brand):
        self.brand = brand          #Public variable by default

    def start(self):                # class method
        print(f"{self.brand} is starting now")  


my_car = Car("Suzuki")          
print(my_car.brand)            # access the class variable

my_car.start()                 # class method call
