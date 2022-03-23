# Define a Function that take list of strings
# List Containing reverse of every String

# NOTE - USE LIST COMPREHENSION because we already did this exercise
# Using Normal Method

# Example
# l = ['abc', 'lmn', 'xyz']
# reverse_String(l) ---> ['cba', 'nml', 'zyx']\

# Solution
def reverse_LC(r):
    inside = [i[::-1] for i in r]
    return inside

print(reverse_LC(['abc', 'lmn', 'xyz']))

# Method 2
def reverse_LC_2(r):
    return [i[::-1] for i in r]
print(reverse_LC_2(['abc', 'lmn', 'xyz']))