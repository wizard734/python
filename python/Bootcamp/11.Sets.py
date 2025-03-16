#Sets:- sets work like tuples but they are not ordered and they are mutable 
#they look like dictonaries but they are not

set1 = {"Roger" , "syd"}
set2 = {"Roger"}

#intersection
intersect = set1 & set2
print(intersect)

#Union
mod = set1 | set2
print(mod)

# -
sub = set1 - set2 
print(sub)

# Subset check

subset = set1 > set2
print(subset)

#count items in list using len function

print(list(set1))


