#Decoraters are the way to change enhance or alter in any way how a function works

def logtime(func):
    
    def wrapper():
        #do something before
        print("before")
        val = func()
        #do something after
        print("After")
        return val
    return wrapper


@logtime
def hello():
    print("hello")

hello()

# Applications
# Change behevior of function without modifying function itself.
# Example:- add logging, test performance, perform caching, verify permissions and so on. 
# Same code on multiple functions

















