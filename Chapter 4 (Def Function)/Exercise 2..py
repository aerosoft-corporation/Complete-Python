# Define pelindrome 
def pelindrome(name):
    if name == name[::-1]:
        return "True"
    else:
        return "False"

name = input("Enter Pelindrome World : ")
print(pelindrome(name))


