# try:
#     #some lines of code
# except EOFError:
#     #handler <ERROR1>
#     print("End of file Error")

# except ZeroDivisionError:
#     #handler <ERROR2>

# else:
#     # no exceptions were raised, the code ran successfully

# finally:
#     #do something in any case

# try:
#     result = 2/0
# except ZeroDivisionError:
#     print('Cannot divide by zero!')
# finally:
#     result = 1

# print(result) #1

# try:
#     raise Exception('An error!')
# except Exception as error:
#     print(error)

class DogNotFoundException(Exception):
    print("Inside")
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found!')

#with keyword helps in simplifying working with exception handling

#Ex: Without with
filename = '/user/flavio/text.txt'

# try:
#     file = open(filename, 'r')
#     content = file.read()
#     print(content)

# finally:
#     file.close()

# Using with 

with open(filename,'r') as file:
    content = file.read()
    print(content)





