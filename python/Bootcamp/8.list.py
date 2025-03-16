dogs = ["Roger","ana","Syd","kay"]

# Can have list of multiple data type

print("Syd" in dogs)
dogs[2] = "tommy"
dogs.extend(["judah" , 5]) #Using "+=" too
print(dogs[-1])

print(dogs[:3])

print(len(dogs))

dogs.remove("tommy")
dogs.pop() 

dogs[1:1] = ["poppy", "olly"] 
dogs.insert(2, "jimy")

#dogs.sort(key=str.lower)

print(sorted(dogs, key = str.lower))# creats new list without modifying old list

dogscopy = dogs[:]
print(dogs)
print(dogscopy)

