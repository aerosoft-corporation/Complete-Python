# Define a function that take list of words as a argument and return list with reverse of every element in that list

# Example
# ['abc', 'xyz', 'lmn', 'tuv'] ----> ['cba', 'zyx', 'nml', 'vut']

# Solution
def reverse_item(l):
    rev = []
    for i in l:
        rev.append(i[::-1])
    return rev

l = ['abc', 'xyz', 'lmn', 'tuv']
total = reverse_item(l)
print(f"Reverse of Every Item is {total}")