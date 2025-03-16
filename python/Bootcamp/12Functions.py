def hello(name, age):
    print('hello! ' + name + ", you are " + str(age) + " years old" )

hello('shivam' , 20)

def change(value):
    value = 2

val =1 # immutable
print(change(val))
#Whatever we change inside the function does not affect outside the function 

print(val)

def change2(value):
    value["name"] = "Syd"

val = {"name":"shivam"} # mutable
change2(val)

print(val)

#return statements

def hello1(name):
        print('Hello'+ name + '!')
        return name, "Beau", 8

print(hello1("Syd"))

#Variable Scope

age = 8 #global scope

def test():
    age = 20
    print(age) #local scope

print(age)
test()

#nested function

def talk(phrase):
    def say(word):
        print(word)
    
    words = phrase.split(' ') # split is a way to create a list out of string
    for word in words:
        say(word)

talk('I am going to buy the milk')

def count():
    count = 0

    def Increment():
        nonlocal count #non local is used to access the variable declared in the parent function in the child function
        count = count + 1
        print(count)

    Increment()

count()

#Closure:-closure is the special way to do the funtion in python
#if you return nested function form the function then that function has access to variable defined in that function even if that function ids not active anymore

def counter():
    count = 0
    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment

increment = counter()

print(increment())
print(increment())
print(increment())







