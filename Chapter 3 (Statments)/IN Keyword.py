# IN keyword is use for checking a Paticular Character/Letter in our String or Variable

# Using Variable.
name = 'abbas'

if "b" in name :
    print("Letter Present.")
else:
    print("Letter Is Not Present.")
    pass
# Using String
if "a" in "abbas":
    print("Letter Present.")
else:
    print ("Letter Is Not Present.")


# Using User Input
name = input("Enter Name : ")
char = input("Enter Letter That You Want To Know : ")
name = name.lower()
char = char.lower()
if char in name:
    print(f"In \"{name}\" Letter \"{char}\" is Present!!!")
else:
    print(f"In \"{name}\" Letter \"{char}\" Is Not Present!!!!")