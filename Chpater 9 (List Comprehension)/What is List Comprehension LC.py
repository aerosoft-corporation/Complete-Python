# list Comprehension
# With the Help of List Comprehension we can create of list in one line

# Tasks
# 1. Create a list of square from 1 to 10
# Simple Method
square = []
for i in range(1, 11):
    square.append(i**2)
print(square)

# With List Comprehension LC
lc_square = [i**2 for i in range(1, 11)]
print(lc_square)


# 2. Negative Numbers
negative = []
for i in range(1, 11):
    negative.append(-i)
print(negative)

# # With List Comprehension
new_negative = [-i for i in range(1, 11)]
print(new_negative)



# 3. First Letter of Names[0]
# Simple Method 
new_names = []
name = ['Abbas', 'Bilal', 'Mubashar']
for i in name:
    new_names.append(i[0])
print(new_names)

# With List Comprehension
new_name = [i[0] for i in name]
print(new_name)