# Num to String
# Define a Function 

# Example
# Input -----> [True, False, [1,2,3], 1, 1.0, 3]
# Output -----> ['1', '1.0', '3']


# 1. With List Comprehension
def int_filter(l):
    return [str(i) for i in l if (type(i) == int or type(i) == float)]

l = [True, False, [1,2,3], 1, 1.0, 3]
print(f"LC with def func >>>> {int_filter(l)}")


# 2. Pure LC
filter2 = [True, False, [1,2,3], 1, 1.0, 3]
new_filter = [str(i) for i in filter2 if (type(i) == int or type(i) == float)]
print(f"LC with Pure Comprehension >>>> {new_filter}")


# 3. With Def Function Simple Code
def int_filter3(l):
    filter = []
    for i in l3:
        if (type(i) == int or type(i) == float):
            filter.append(str(i))
    return filter

l3 = [True, False, [1,2,3], 1, 1.0, 3]
print(f"Default Method Without LC >>>> {int_filter3(l3)}")


# 4. Without def function
l4 = [True, False, [1,2,3], 1, 1.0, 3]
filter = []
for i in l4:
    if (type(i) == int or type(i) == float):
        filter.append(str(i))
print(f"Without def and LC >>>> {filter}")