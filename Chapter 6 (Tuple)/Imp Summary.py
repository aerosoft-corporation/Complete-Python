# Tuple 
# Tuples are immutable
# Tuples are orderedd collection on item
# Tuples can store any type of data
# You cannot change (add or delete) values from tuple once it created 
# but can add, delete data from list which is present inside tuple 
mixed = (1,2,3,4,5.0)
# no.appen(), no pop(), no.insert(), no.remove()
# only count(), and index()

# Function 
# min(), max(), sum()


mixed2 = (1,2,3,4,5,[6,7,8])
mixed2[5].insert(3, 9)
print(mixed2)

# we don't use list inside tuple bcoz it impact the speed of tuple 