

class A:
    def show(self):
        print("In A")

class B(A):
    def show(self):
        print("In B")

class C(A):
    def show(self): 
        print("In C")

class D(B,C):
    pass

print(D.mro())   # Method Resolution Order
d = D()
d.show()

