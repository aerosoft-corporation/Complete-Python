# In keyword and iteration in dictionary
# Method uses (items(), keys(), values())

user_info = {
    'name' : 'Abbas Ali',
    'age' : 21,
    'fav_movies' : ['The Martian', 'Rio'],
    'fav_Singer' : ['Edward Maya', 'Akcent']
}
# Checking Values() Method
user_info_keys_check = user_info.keys()
print(user_info_keys_check)
print(type(user_info_keys_check))

# Checking keys() Method 
user_info_values_check = user_info.values()
print(user_info_values_check)
print(type(user_info_values_check))

# Checking items() Method
user_info_items_check = user_info.items()
print(user_info_items_check)
print(type(user_info_items_check))


# 1. Check if key exist in dictionary
# For keys in checking in dictionary
# Method - (.keys())
# It  is default check the keys but if we use the keys() method to check
# Synatx - 1
user_info_keys = user_info.keys()
if "name" in user_info_keys:
    print('Present')
else:
    print('Not Present')

# # Syntax - 2

if 'name' in user_info.keys():
    print('Present')
else:
    print('Not Present')

# 2. Check if value exist in dictionary
# For values checking in dictionary
# Method - (values())
# Syntax - 1
user_info_values = user_info.values()
if 'Abbas Ali' in user_info_values:
    print('Present')
else:
    print('Not Present')

# # Syntax - 2

if 'Abbas Ali' in user_info.values():
    print('Present')
else:
    print('Not Present')

# 3. Looping in Dictionaries

for i in user_info:      #It will print the keys in dictionaries
    print(i)

# 2.   
for i in user_info.keys():    #This Methid will also check for keys
    print(i)

# 3. 
for i in user_info.values():    #This method will print the values in dictionary
    print(i)

# # 4. 
for i in user_info:    #this method will also print the values in dictionaries
    print(user_info[i])

# 5. 
for i in user_info.items():    #This Mehtod is very usefull. it prints all your dictionary keys + values
    print(i)

# 6. 
# dictionary unpacking
for i,j in user_info.items():
    print(f"The key is {i} and the value is {j} ")