done = ""

if done:
    print("yes")
else:
    print("no")

#strings are false only if they are empty

book_1_read=True
book_2_read=False

read_any_book = any([book_1_read,book_2_read])
print(read_any_book)

read_all_book = all([book_1_read,book_2_read])
print(read_all_book)

num1 = 2+3j
num = complex(2,3)

print(num.real,num.imag)

print(abs(-5.5))

print(round(3.14))

from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value)
print(State.ACTIVE)
print(State[1])
print(State['ACTIVE'].value)

print(list(State))