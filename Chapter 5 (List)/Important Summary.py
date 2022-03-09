# You can store any type of data in list
# Liat is ordered collection of item
mixed = [1,2,3, [4,5,6], 'seven', 8.0, None]
print(mixed[3])
print(mixed[0])
print(mixed)

# For Adding data in list

# Append Method
mixed.append("10")
mixed.append([10, 20, 30])   #Adding Extra List in List
print("Append Method =", mixed)
# Extend Method
mixed.extend([10, 20, 30])   #Adding Only Item 
print("Extend Method =", mixed)
# Insert Mehthod
mixed.insert(0,0)
print("Insert Method =",mixed)  #Adding Data By positional


# 2. Joining List

# Join Two list
l1 = [1,2,3]
l2 = [4,5,6]
#String Method
l3 = l1 + l2
print("Joining List =",l3)
# Extend Method > This method is right for joining two list
l1.extend(l2)
print("Extend Method =", l1)
# Append Method > Adding List inside extra List
l1.append(l2)
print("Append Method =", l1)

 
# 3. For Removing Data in List

# Note: Pop() method return the value which they have removed/pop
# Pop Method 
popped = mixed.pop()   #Remmoving Last Item In our list
popped1 = mixed.pop(1)    #Removing Selected Item
print(popped)
print(popped1)
print(mixed) 


# delete function/operator
del mixed[0]
print(mixed)


# Remove Method 
# Note: When we don't know the position of an item then we use remove method
mixed.remove(8.0)
print(mixed)



# 4. Looping In List
for i in mixed:
    print(i, end=',')


    # ###################################### THE END ############################################