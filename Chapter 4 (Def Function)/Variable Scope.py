# Variable Scope
x = 5     #Global Variable
def func():
    global x
    x = 10      # Local Variable 
    return x

print(x)
print(func())