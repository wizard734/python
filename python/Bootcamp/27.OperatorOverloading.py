
class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __gt__(self, other):
        return True if self.age > other.age else False

roger = Dog('Roger',8)
syd = Dog('Syd', 7)

print(roger>syd)
