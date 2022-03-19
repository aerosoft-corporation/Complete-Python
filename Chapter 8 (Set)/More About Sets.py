# In Keyword and Loops in Sets
s= {'a', 'b', 'c'}

# In Keyword to check if item is present or not in set
if 'a' in s:
    print('present')
else:
    print('Not Present')

# Loop (For Loop)
for i in s:
    print(i)


# Some Mathimatical Operation (Union, Intersection)
# 1. Union
s1 = {1,2,3,4}
s2 = {3,4,5,6}
union_set = s1 | s2
print(f"Union Is : {union_set}")

# Intersection
intersection_set = s1 & s2
print(f"Intersection Is : {intersection_set}")