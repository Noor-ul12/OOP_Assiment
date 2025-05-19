
from abc import abstractmethod, ABC

class shape(ABC):
    @abstractmethod
    def area(self):  # abstract method
        pass

class rectangle(shape):   # inheritance

    def __init__(self,width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = rectangle(3,4)
print(rect.area())
           