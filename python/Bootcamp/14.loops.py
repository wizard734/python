
condition = True
while condition == True:
    print("the condition is true")
    condition = False

count = 0
while count < 10:
    print("the condition is true") 
    count += 1

print("after the loop")

items = [1 ,2 ,3]
for item in items:
    print(item)

for i in range(15):
    print(i)

b =[1,2,3,4,5]
for index, b1 in enumerate(b):
    print(index, b1)

#break: stops complete loop
#continue: skip the current loop

item = [1 ,2 ,3]
for ite in item:
    if(ite == 2):
        continue
    print(ite)

item = [1 ,2 ,3]
for ite in item:
    if(ite == 2):
        continue
    print(ite)

    