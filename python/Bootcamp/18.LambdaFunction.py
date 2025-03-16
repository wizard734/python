lambda num:num * 2

multiply = lambda a,b : a*b

print(multiply(2,4))

#Map(),Filter(),reduce()

#Map is a function used to run a function upon each item in an iterable item(like list) and create a list of same number of items but the values of  each item can be changed 
  
numbers = [1, 2, 3]
#def double(a):
    #return a*2

#double = lambda a: a*2

#result = map(double, numbers)

#print(list(result))

#more simplified

result = map(lambda a : a*2, numbers)
print(list(result))

#filter:- filter takes a iterable and returns afilter object which is another iterable but without some od the original items
# it returns true or false


res1 = filter(lambda a: a%2==0, numbers)
print(list(res1))

#Reduce :- It is used to calculate a value out of sequence like
from functools import reduce
expenses = [
    ('Dinner', 80),
            ('car repair',120)
]

sum = 0
#without reduce
#for expanse in expenses:
#   sum += expanse[1]

#with reduce

sum = reduce(lambda a,b: a[1] + b[1], expenses)


print(sum)





