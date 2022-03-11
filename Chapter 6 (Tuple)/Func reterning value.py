def func(int1, int2):
    add = int1 + int2
    multiply = int1 * int2
    return add, multiply
# NOTE - Whenever we are returning two or more than two value then we recieve a Tuple

# Tuple Returning
int1 = 2
int2 = 3
total = func(int1, int2)
print(total)

# Simple Value returning
add , multiply = func(2,3)
print(add, multiply)
# OR
print(add)
print(multiply)

