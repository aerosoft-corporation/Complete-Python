def Addition(a,b):
    return a + b
def Subtract(a,b):
    return a - b
def Multiply(a,b):
    return a * b
def Division(a,b):
    return a / b
def NonF_Division(a,b):
    return a // b

# a = int(input("Enter First Number : "))
# b = int(input("Enter Second Number : "))

print('Addition (+)')
print('Subtract (-)')
print('Multiply (*)')
print(' Fractional Divide (/)')
print('Non Fractional Divide (//)')
user_input = input("Enter Operator Name : ")
# For Addition >>>>
if user_input == "+" or user_input == "+":
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))
    total = Addition(a,b)
    print(f"Total is {total}")
# For Subtraction >>>>
elif user_input == "-":
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))
    total = Subtract(a,b)
    print(f"Total is {total}")
# For Multiplictaiaon >>>>
elif user_input == "*":
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))
    total = Multiply(a,b)
    print(f"Total is {total}")
# For Fractional Division 
elif user_input == "/":
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))
    total = Division(a,b)
    print(f"Total is {total}")
# For Non Fractional Division
elif user_input == "//":
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))
    total = NonF_Division(a,b)
    print(f"Total is {total}")    
else:
    None