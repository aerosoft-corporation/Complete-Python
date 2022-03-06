# Q1.Ask User for two numbers and print bigger  number of both inputs
# Solution
def greater (a,b):
    if a > b:
        return a
    else:
        return b
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
total = greater(a, b)
print("Bigger Number is " + str(total))