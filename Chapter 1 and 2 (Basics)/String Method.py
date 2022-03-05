# String Method Part #1
# name = "Abbas_Ali"

# 1. Len() Function   #Finding characters lenght

# print(len(name))   #USING VARIABLE

print (len("abbas"))     #USING PRINT FUNCTION

# 2. Upper() Function    #change letters into capital letters

print("Abbas".upper())  #USING PRINT FUNCTION

# print(name.upper())    #USING VARIABLE

# 3. Lower() Function   #change letters into small letters

# print (name.lower())       #USING VARIABLE

print("ABBAS".lower())      #USING PRINT FUNCTION

# 4. Title() Function     #Change first letter into capital

print("abbas".title())   #USING PRINT FUNCTION

# print(name.title())   #USING VARIABLE

# 5. Count Function       #count number which you want (capital and small letters matters)  # enter your input is allways in String ("")

# print(name.count(""))    #USING VARIABLE

print("abbas".count("a"))    #USING PRINT FUNCTION

# exercise
name, char = input("what is your name and char").split(",")
# # String Format Method
print(f"lenght of your name is: {len(name) }")
print(f"character count:{name.strip().lower().count(char.strip().lower())}")
# # Normal Print Method
# print("lenght of your name is :", len(name))
# print("character count is : ", name.strip().lower().count(char.strip().lower()))
