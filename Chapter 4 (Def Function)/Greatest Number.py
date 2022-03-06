def greatest (a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# no_one = int(input("Enter First Number : "))
# no_two = int(input("Enter Second Number : "))
# no_three = int(input("Enter Third Number : "))
total = greatest(1000, 5000, 100)
print(total)