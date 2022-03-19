# Set Data Type
# Unordered Collection Of Unique Items
# Set() donot store Duplicate items
# We cannot store List(), Tuple(), Dict() in Set()
# Syntax 
s = {1, 2, 3}
# We cannot use indexing bcoz of unordered collection 
# print(s[0])  --->  Error

# Q - Why we use Set()
# A - To remove Duplicate Elements
# Example
l = [1,2,3,4,4,4,5,5,6,6,6,7,7,7,8,8,2,9,9,9,9]
s1 = list(set(l))  #--> Remember this method 
print(s1)

d = {1, 1.0, 2.3, "String", [1], {1:1}, (1,1)}    # We cannot store List(), Tuple(), Dict() in Set()
# Note -  1 and 1.0 are the same for the set(). 1 and 1.1 are not same for the set
print(d)  # --->  Error

# Some Method of Set()

# Add Data in Set
s.add(4)
s.add(5)
s.add(4)
# print(s)


# 1. To Remove Data in Set
s.remove(3)
s.remove(2)
# print(s)


# 2. Remove Method ---> No Error
# if written element exist in set the discard method remove-
# and if element does not exist in set the discard method will not declare error
s.discard(1)
# print(s)


# Copy Method 
s2 = s.copy()
# print(s2)


# Clear Method
s.clear()
print(s)
