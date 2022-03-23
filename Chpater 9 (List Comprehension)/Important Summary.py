# List Comprehension Summary

# 1. LC with loop
# Example (Square List)
square = [i**2 for i in range(1,11)]
print(square)


# 2. LC with If Statement
# Example (Odd-Even)

# Even Numbers
even = [i for i in range(1,11) if (i%2 == 0)]
print(even)
# Odd Numbers
odd = [i for i in range(1,11) if (i%2 != 0)]
print(odd)


# 3. LC with If else
# Example - 
mixed = [i*2 if (i%2 == 0) else -i for i in range(1,11)]
print(mixed)


# 4. Nested List
# Example ---> [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
nest_list = [[i for i in range(1,4)] for j in range(3)]
print(nest_list)