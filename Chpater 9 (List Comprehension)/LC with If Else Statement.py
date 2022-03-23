# List Comprehension with if else
# Code Structure when if else exist ---> [i if statement, then else, then loop]
nums = [1,2,3,4,5,6,7,8,9,10]
# Output = [-1, 4, -3, 8, -5, 12, -7, 16, -9]
# With Simple Method
new_list = []
for i in nums:
    if i%2 == 0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(new_list)

# With LC 
new_list2 = [i*2 if (i%2 == 0) else -i for i in range(1, 11)]
print(new_list2)