# 1. Range function with list
lst = list(range(1, 11))
print(lst)

# 2. More about pop() method
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number.pop())     #pop() method returns the value which they have remove


# 3. index() Mrhtod 
number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number1.index(5,3,5))     # Give the location of a specific item  .index(value, starting, specific start)


# 4. Returning Negative List

number2 = list(range(1, 11))
# number2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def negative(n):
    negative = []
    for i in n:
        negative.append(-i)
    return negative

print(negative(number2))