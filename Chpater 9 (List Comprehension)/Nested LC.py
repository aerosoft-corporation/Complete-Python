# Nested List With Nested List
# Example = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# With List Comprehesnion
nested = [[i for i in range(1, 4)] for j in range(3)]
print(nested)

# Simple Method
new_list = []
for i in range(3):
    new_list.append([1,2,3])
print(new_list)

