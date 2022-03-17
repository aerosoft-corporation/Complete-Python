# Eercise No.1
# define a function that takes a number(n)
# return a dictionary containing cube of numbers from 1 to n
# Example
# cube_finder(3)
# {1:1, 2:8, 3:27}

# Solution
def cube_finder(n):
    cubes = {}
    for i in range(1, n+1):
        cubes[i] = i**3
    return cubes

n = int(input("Enter Number : "))
print(cube_finder(n))