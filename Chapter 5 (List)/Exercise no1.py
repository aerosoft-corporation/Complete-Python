# Define a function which will take list containing number as input and return list containing square of every element.

# Example 
# number = [1, 2, 3, 4]
# Square_list(number) ----> return ----> [1, 4, 9, 16]


# Solution
def square_list(s):
    square = []
    for i in s:
        square.append(i**2)
    return square

number = list(range(1, 11))
total = square_list(number)
print(f"Square List = {total}")