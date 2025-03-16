dog={ "name" : "Roger" , "age" : 8, "color" : "green"}

#dog["name"] = "Syd"

print(dog.get("color" ,"brown"))

#print(dog.pop("name"))
#print(dog.popitem())

print("color" in dog)

#print(dog.keys())
print(list(dog.keys())) #return list part

print(list(dog.items()))

print(len(dog))

#adding new k, val pair

dog["favorite food"] = "Meat"

#Deleating

del dog["color"]

#copy

dogCopy = dog.copy()



print(dog)