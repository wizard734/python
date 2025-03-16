
class Animal:
    def walk(self):
        print("Walking...") 

class Dog(Animal):
    def __init__(self , name, age):
        self.name = name
        self.age = age
    
    def bark(self): #self:- is the argument to the method will point to current object instance and must be specified while defining a method
        print("woof!")

roger = Dog("Roger", 8)

print(roger.name)

print(roger.bark())

print(roger.walk())




